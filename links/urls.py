from django.urls import path

from links.views import LinkListView, LinkCreateView, LinkDetailView


app_name = 'links'
urlpatterns = [
    path('', LinkListView.as_view(), name='list'),
    path('create/', LinkCreateView.as_view(), name='create'),
    path('<int:pk>/', LinkDetailView.as_view(), name='detail'),
]
