# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 

from .views.hydrant_views import HydrantViewSet
from .views.user_views import UserViewSet
from .views.review_views import ReviewViewSet
from .models.hydrant import Hydrant

router = routers.DefaultRouter()
router.register(r'hydrants', HydrantViewSet)
router.register(r'users', UserViewSet)
router.register(r'reviews', ReviewViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]
