from django.urls import path

from links.views import LinkListView, LinkCreateView, LinkDetailView


app_name = 'links'
urlpatterns = [
    path('link-list/', LinkListView.as_view(), name='link-list'),
    path('link-create/', LinkCreateView.as_view(), name='link-create'),
    path('link-detail/<int:pk>/', LinkDetailView.as_view(), name='link-detail'),
]
