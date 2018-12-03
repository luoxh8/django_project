from django.urls import path

from goods.views import BidAPIView, GoodsCategoryDetailAPIView, GoodsDetailAPIView, GoodsListAPIView, NewsAPIView

urlpatterns = [
    path('list', GoodsListAPIView.as_view()),
    path('detail', GoodsDetailAPIView.as_view()),
    path('category/detail', GoodsCategoryDetailAPIView.as_view()),
    path('category/list', GoodsListAPIView.as_view()),
    path('news', NewsAPIView.as_view()),
    path('bid', BidAPIView.as_view()),
]
