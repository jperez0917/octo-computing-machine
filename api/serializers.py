from rest_framework import serializers

from django.contrib.auth import get_user_model

from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

