from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
# router.register('users', views.UserViewSet, basename='users')
router.register('links', views.LinkViewSet, basename='links')
router.register('public', views.LinkPublicViewSet, basename='public')

urlpatterns = router.urls + [
    path('currentuser/', views.CurrentUserView.as_view())
]
