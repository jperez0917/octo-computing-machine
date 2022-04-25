from rest_framework import viewsets

from django.contrib.auth import get_user_model

from api.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

