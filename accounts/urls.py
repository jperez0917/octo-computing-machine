from django.urls import path

from accounts.views import SignUpView, UserProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='profile'),
]
