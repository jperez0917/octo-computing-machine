from rest_framework import viewsets, generics, permissions

from django.contrib.auth import get_user_model

from api.serializers import UserSerializer, LinkSerializer
from links.models import Link

class LinkPublicViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List of Links where the 'public' field is set to True. These Links are for public view by anonymous users.
    """
    queryset = Link.objects.filter(public=True)
    serializer_class = LinkSerializer


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticated,)


class LinkViewSet(viewsets.ModelViewSet):
    """
    Links which are owned by user. Should allow adding Link by user.
    """
    def get_queryset(self):
        return Link.objects.filter(owner=self.request.user.id)
    serializer_class = LinkSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CurrentUserView(generics.RetrieveAPIView):
    """
    User info and Links owned by user.
    """
    serializer_class = UserSerializer
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
    permission_classes = (permissions.IsAuthenticated,)
