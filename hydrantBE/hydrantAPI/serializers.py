# serializers.py
from rest_framework import serializers
from .models.hydrant import Hydrant

from django.contrib.auth import get_user_model # If used custom user model
UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ("id", "username", "password", "email")

class HydrantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hydrant
        fields = ('id', 'name', 'description', 'long', 'lat', 'created_at', 'updated_at')

