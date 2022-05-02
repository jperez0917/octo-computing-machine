from django.urls import path

from links import views

app_name = 'links'
urlpatterns = [
    path('', views.PublicLinkListView.as_view(), name='public'),
    path('profile/', views.LinkUserProfileView.as_view(), name='profile'),
    path('create/', views.LinkCreateView.as_view(), name='create'),
    path('<int:pk>/', views.LinkDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.LinkUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.LinkDeleteView.as_view(), name='delete'),
]
