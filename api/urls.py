from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, LinkViewSet


router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('links', LinkViewSet, basename='links')

urlpatterns = router.urls + [
    
]
