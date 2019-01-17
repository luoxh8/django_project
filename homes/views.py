from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView

from goods.models import BidRecord, Goods
from h_utils.errors import ErrBaseNotData
from h_utils.response_extra import success_request, error_request
from h_utils.serializers_extra import serializer_list_data
from h_utils.success import array_success, dict_success
from homes.models import Banner, Topic
from homes.serializers import (BannerSerializer,
                               IAmShootingSerializer,
                               MyCollectionSerializer,
                               RecommendSerializer,
                               TopicSerializer)
from user_operation.models import Collection


class IndexAPIView(APIView):

    @staticmethod
    def get(request):
        banner_list = Banner.objects.all()
        topic_list = Topic.objects.all()

        if not banner_list and not topic_list:
            return error_request(ErrBaseNotData)

        return_data = dict_success()
        return_data['data']['banner'] = serializer_list_data(banner_list, BannerSerializer, request)
        return_data['data']['topic'] = serializer_list_data(topic_list, TopicSerializer, request)
        return success_request(return_data)


class RecommendAPIView(APIView):

    @staticmethod
    def get(request):
        goods_list = Goods.objects.filter(is_hot=True).all()

        if not goods_list:
            return error_request(ErrBaseNotData)

        return_data = array_success()
        return_data['data'] = serializer_list_data(goods_list, RecommendSerializer, request)
        return success_request(return_data)


class GuessYouLikeAPIView(APIView):

    @staticmethod
    def get(request):
        goods_list = Goods.objects.filter(is_new=True).all()

        if not goods_list:
            return error_request(ErrBaseNotData)

        return_data = array_success()
        return_data['data'] = serializer_list_data(goods_list, RecommendSerializer, request)
        return success_request(return_data)


class IAmShootingAPIView(APIView):
    permission_classes = (IsAuthenticated,) or (IsAdminUser,)

    @staticmethod
    def get(request):
        br_list = BidRecord.objects.filter(profile__username=request.user).all()
        if not br_list:
            return error_request(ErrBaseNotData)
        return_data = array_success()
        return_data['data'] = serializer_list_data(br_list, IAmShootingSerializer, request)
        return success_request(return_data)


class MyCollectionAPIView(APIView):
    permission_classes = (IsAuthenticated,) or (IsAdminUser,)

    @staticmethod
    def get(request):
        collection = Collection.objects.filter(user__username=request.user).all()

        if not collection:
            return error_request(ErrBaseNotData)

        return_data = array_success()
        data = serializer_list_data(collection, MyCollectionSerializer, request)
        print(data)
        return_data['data'] = None
        return success_request(return_data)

    @staticmethod
    def post(request):
        pass
