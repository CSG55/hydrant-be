# serializers.py
from rest_framework import serializers
from .models.hydrant import Hydrant
from .models.review import Review

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
    created_by_id = serializers.ReadOnlyField(source='created_by.id', read_only=True)
    class Meta:
        model = Hydrant
        fields = ('id', 'created_by_id', 'name', 'description', 'long', 'lat', 'created_at', 'updated_at')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    # hydrant_id = serializers.ReadOnlyField(source='hydrant.id', read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'hydrant_id', 'created_by', 'review_text', 'rating', 'created_at', 'updated_at')

