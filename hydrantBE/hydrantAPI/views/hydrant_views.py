from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from hydrantAPI.serializers import HydrantSerializer
from hydrantAPI.models.hydrant import Hydrant


class HydrantViewSet(viewsets.ModelViewSet):
    queryset = Hydrant.objects.all()
    serializer_class = HydrantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']
    

