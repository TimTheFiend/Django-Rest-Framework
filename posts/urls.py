# from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet


ROUTER = SimpleRouter()
ROUTER.register('users', UserViewSet, basename='users')
ROUTER.register('', PostViewSet, basename='posts')


urlpatterns = ROUTER.urls
