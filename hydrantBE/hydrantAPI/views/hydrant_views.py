from django.shortcuts import render
from rest_framework import viewsets

from hydrantAPI.serializers import HydrantSerializer
from hydrantAPI.models.hydrant import Hydrant


class HydrantViewSet(viewsets.ModelViewSet):
    queryset = Hydrant.objects.all().order_by('name')
    serializer_class = HydrantSerializer
