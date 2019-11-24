from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets

from django.contrib.auth.models import User
from hydrantAPI.serializers import UserSerializer


class CreateUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer
