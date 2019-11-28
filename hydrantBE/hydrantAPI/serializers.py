from django.contrib.auth.decorators import login_required
from rest_framework import serializers
from .models.hydrant import Hydrant
from .models.review import Review
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password']) # set_password encrypts the password text
        user.save()

        return user
    class Meta:
        model = UserModel
        fields = ("id", "username", "password", "email")

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    hydrant_id = serializers.IntegerField(source='hydrant.id')
    def create(self, validated_data):

        hydrant_id = self.initial_data['hydrant_id']
        if not Hydrant.objects.filter(id=hydrant_id).count():
            raise serializers.ValidationError("The hydrant id provided does not exist.")
        print(self.context['request'].user.id)
        review = Review.objects.create(
            rating=validated_data['rating'],
            title=validated_data['title'],
            review_text=validated_data['review_text'],
            created_by_id = self.context['request'].user.id, # id of current logged-in user is set to created_by_id
            hydrant_id = self.initial_data['hydrant_id']
        )

        review.save()
        return review


    class Meta:
        model = Review
        fields = ('id', 'title', 'hydrant_id', 'created_by_id', 'review_text', 'rating', 'created_at', 'updated_at')


class HydrantSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(source='review_set', many=True, read_only=True) # include reviews associated with hydrants
    def create(self, validated_data):
        hydrant = Hydrant.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            long=validated_data['long'],
            lat=validated_data['lat'],
            image_url=validated_data['image_url'],
            created_by_id = self.context['request'].user.id # id of current logged-in user is set to created_by_id
        )
        hydrant.save()
        return hydrant

    class Meta:
        model = Hydrant
        fields = ('id', 'name', 'created_by_id', 'description', 'created_at', 'updated_at', 'long', 'lat', 'image_url', 'reviews')
