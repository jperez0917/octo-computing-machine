from rest_framework import viewsets, generics, permissions

from django.contrib.auth import get_user_model

from api.serializers import UserSerializer, LinkSerializer
from api.permissions import IsOwnerOrReadOnly
from links.models import Link


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
    permission_classes = (permissions.IsAuthenticated,)
