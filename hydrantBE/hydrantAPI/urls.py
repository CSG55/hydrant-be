# myapi/urls.py
from django.urls import include, path
from rest_framework import routers

from .views.hydrant_views import HydrantViewSet
from .views.user_views import CreateUserView
from .models.hydrant import Hydrant

router = routers.DefaultRouter()
router.register(r'hydrants', HydrantViewSet)
router.register(r'users', CreateUserView, basename='CreateUser')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
