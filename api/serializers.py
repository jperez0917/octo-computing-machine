from rest_framework import serializers

from django.contrib.auth import get_user_model

from links.models import Link


class NestedLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = (
            'id',
            'url_label',
            'url',
            'notes',
            'public',
            )


class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            )


class LinkSerializer(serializers.ModelSerializer):
    owner_detail = NestedUserSerializer(read_only=True, source='owner')
    class Meta:
        model = Link
        fields = (
            'id',
            'url_label',
            'url',
            'notes',
            'public',
            'owner',
            'owner_detail',
            )


class UserSerializer(serializers.ModelSerializer):
    links_detail = NestedLinkSerializer(read_only=True, many=True, source='links')
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'links_detail',
            )


