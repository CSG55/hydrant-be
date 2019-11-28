# myapi/urls.py
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from .views.hydrant_views import HydrantViewSet
from .views.user_views import UserViewSet, CustomObtainAuthToken
from .views.review_views import ReviewViewSet
from .models.hydrant import Hydrant

router = routers.DefaultRouter()
router.register(r'api/hydrants', HydrantViewSet)
router.register(r'api/users', UserViewSet)
router.register(r'api/reviews', ReviewViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/authenticate/', CustomObtainAuthToken.as_view()),

]
