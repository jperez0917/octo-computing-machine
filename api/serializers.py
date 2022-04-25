from rest_framework import serializers

from django.contrib.auth import get_user_model

from links.models import Link

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ('id', 'url_label', 'url', 'public', 'owner')


