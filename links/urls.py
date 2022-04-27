from django.urls import path

from links.views import LinkListView, LinkDetailView
from links.views import LinkCreateView, LinkEditView, LinkDeleteView

app_name = 'links'
urlpatterns = [
    path('', LinkListView.as_view(), name='list'),
    path('create/', LinkCreateView.as_view(), name='create'),
    path('<int:pk>/', LinkDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', LinkEditView.as_view(), name='edit'),
    path('<int:pk>/delete/', LinkDeleteView.as_view(), name='delete'),
]
