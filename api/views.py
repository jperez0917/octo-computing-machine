from rest_framework import viewsets, generics, permissions

from django.contrib.auth import get_user_model

from api.serializers import UserSerializer, LinkSerializer
from links.models import Link

class LinkPublicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Link.objects.filter(public=True)
    serializer_class = LinkSerializer


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticated,)


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    #################################################################
    # When user not authenticated:

    # permission_classes = ()
    # # {
    # # "id": null,
    # # "username": "",
    # # "links_count": 0
    # # }

    # permission_classes = (permissions.IsAuthenticated,)
    # # {
    # # "detail": "Authentication credentials were not provided."
    # # }
    #################################################################
    def get_object(self):
        return self.request.user
