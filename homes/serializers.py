from rest_framework import serializers

from goods.models import BidRecord, Goods
from homes.models import Banner, Topic


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = (
            'title',
            'image',
            'index',
            'url',
            'activity',
            'goods_id',
        )
        depth = 1


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        exclude = (
            'id',
            'is_delete',
            'created_time',
            'updated_time',
        )


class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = (
            'name',
            'goods_id',
            'goods_front_image',
            'now_price',
        )


class IAmShootingSerializer(serializers.ModelSerializer):
    class GoodsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Goods
            fields = (
                'name',
                'goods_id',
                'goods_front_image',
                'now_price',
            )

    goods = GoodsSerializer()

    class Meta:
        model = BidRecord
        fields = (
            'goods',
            'is_out'
        )
        depth = 1


class MyCollectionSerializer(serializers.ModelSerializer):
    class GoodsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Goods
            fields = (
                'name',
                'goods_id',
                'goods_front_image',
                'now_price',
            )

    goods = GoodsSerializer()

    class Meta:
        model = BidRecord
        fields = (
            'goods',
        )
        depth = 1
