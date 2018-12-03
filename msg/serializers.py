from rest_framework import serializers

from msg.models import Msg


class MsgListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Msg
        fields = (
            'id',
            'title',
            'msg_type',
        )


class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Msg
        fields = (
            'id',
            'title',
            'msg_type',
            'content',
            'periods',
        )
