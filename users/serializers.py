from rest_framework import serializers

from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'uid',
            'gender',
            'nick',
            'oauth_avatar',
            "phone",
            'avatar',
            'oauth_avatar',
        )
