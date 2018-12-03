from django.urls import path

from user_operation.views import FavoriteProductAPIView

urlpatterns = [
    path('favoriteProduct', FavoriteProductAPIView.as_view()),
]
