from django.urls import path

from links.views import LinkListView


app_name = 'links'
urlpatterns = [
    path('link-list/', LinkListView.as_view(), name='link-list')
]
