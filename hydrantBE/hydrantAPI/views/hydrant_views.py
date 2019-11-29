from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Avg

from hydrantAPI.serializers import HydrantSerializer
from hydrantAPI.models.hydrant import Hydrant


class HydrantViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Hydrant.objects.all() 
    serializer_class = HydrantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'long', 'lat']

    # overriding default queryset to handle searching by "review__rating" foreign key
    def get_queryset(self):
        queryset = Hydrant.objects.all() 

        rating = self.request.query_params.get('rating')

        if rating: # we filter by the average of all review (fkeys) ratings 
            queryset = queryset.annotate(avg_rating=Avg('review__rating'))\
                .filter(avg_rating__startswith=rating)

        return queryset
