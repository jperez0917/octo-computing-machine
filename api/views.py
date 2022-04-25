from rest_framework import viewsets

from django.contrib.auth import get_user_model

from api.serializers import UserSerializer, LinkSerializer
from links.models import Link


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

