from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from django.contrib.auth.models import User
from hydrantAPI.serializers import UserSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsSuperUser, ]
        elif self.action == 'retrieve':
            self.permission_classes = [IsUser]
        return super(self.__class__, self).get_permissions()


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        return Response({
            'id': user.id, 
            'username': user.username,
            'email': user.email,
            'token': token.key,
        })

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class IsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj == request.user
        else:
            return False
