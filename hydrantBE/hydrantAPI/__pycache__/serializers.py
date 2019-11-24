# serializers.py
from rest_framework import serializers
from models.hydrant import Hydrant

class HydrantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hydrant
        fields = ('name', 'description', 'long', 'lat', 'created_at', 'updated_at')
