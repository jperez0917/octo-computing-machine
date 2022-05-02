from django.urls import path

from accounts import views
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='update'),
]
