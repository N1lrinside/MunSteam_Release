from rest_framework import serializers

from .models import UserFriends


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFriends
        fields = '__all__'

