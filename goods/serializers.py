from rest_framework import serializers

from goods.models import Category, Goods, GoodsImage


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        exclude = (
            'id',
            'is_delete',
            'created_time',
            'updated_time',
            'goods'
        )


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        exclude = (
            'id',
            'is_delete',
            'created_time',
            'updated_time',
            'goods_sn',
            'category',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = (
            'id',
            'is_delete',
            'created_time',
            'updated_time',
        )


class GoodsDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        exclude = (
            'id',
            'is_delete',
            'created_time',
            'updated_time',
            'goods_sn',
        )
        depth = 1

