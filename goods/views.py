from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView

from goods.models import Goods, GoodsImage
from goods.serializers import GoodsCategorySerializer, GoodsDetailSerializer, GoodsImageSerializer
from h_utils.response_extra import (err_base_not_data,
                                    err_base_params,
                                    err_base_server,
                                    err_goods_bid,
                                    err_goods_bidding,
                                    err_goods_not_found,
                                    success_request)
from h_utils.serializers_extra import serializer_data, serializer_list_data
from h_utils.success import array_success, dict_success, normal_success
from users.models import Balance


class GoodsCategoryDetailAPIView(APIView):

    @staticmethod
    def get(request):
        try:
            category_id = request.query_params['category_id']
        except KeyError:
            return err_base_params()
        goods_list = Goods.objects.filter(category_id=int(category_id))
        if not goods_list:
            return err_base_not_data()

        return_data = array_success()
        return_data['data'] = serializer_list_data(goods_list, GoodsCategorySerializer, request)
        return success_request(return_data)


class GoodsDetailAPIView(APIView):

    @staticmethod
    def get(request):
        try:
            goods_id = request.query_params['goods_id']
        except KeyError:
            return err_base_params()

        goods = Goods.objects.filter(goods_id=goods_id).first()

        if not goods:
            return err_base_not_data()
        goods_image_list = GoodsImage.objects.filter(goods_id=goods.id).all()
        return_data = dict_success()
        return_data['data'] = serializer_data(goods, GoodsDetailSerializer, request)
        return_data['data']['goods_images'] = serializer_list_data(goods_image_list, GoodsImageSerializer, request)
        return success_request(return_data)


class GoodsListAPIView(APIView):

    @staticmethod
    def get(request):
        goods_list = Goods.objects.all()

        if not goods_list:
            return err_goods_not_found()


        return_data = array_success()
        return_data['data'] = serializer_list_data(goods_list, GoodsDetailSerializer, request)
        return success_request(return_data)


class NewsAPIView(APIView):

    @staticmethod
    def get(request):
        pass


bid_array = []


class BidAPIView(APIView):
    permission_classes = (IsAuthenticated,) or (IsAdminUser,)

    def can_bid(self, goods, balance):
        if balance.balance >= goods.step_price:
            return True
        return False

    def check_bid(self, request):
        # 检查是否在支付数组里面
        if request.user in bid_array:
            return err_goods_bidding()

        # 添加对象到支付数组
        bid_array.append(request.user)

    # 从支付数组里面移除对象
    def remove_bid(self, request):
        bid_array.remove(request.user)

    def post(self, request):
        try:
            goods_id = request.data['goods_id']
        except KeyError:
            return err_base_params()

        self.check_bid(request)

        goods = Goods.objects.filter(goods_id=goods_id).first()
        balance = Balance.objects.filter(user__username=request.user).first()

        if not balance or not goods:
            self.remove_bid(request)
            return err_base_server()

        if not self.can_bid(goods, balance):
            self.remove_bid(request)
            return err_goods_bid()

        balance.balance -= goods.step_price
        goods.now_price += 0.1
        balance.save()
        goods.save()
        self.remove_bid(request)
        return_data = normal_success()
        return_data['msg'] = '出价成功'
        return success_request(return_data)
