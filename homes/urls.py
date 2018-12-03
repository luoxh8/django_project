from django.urls import path

from homes.views import GuessYouLikeAPIView, IAmShootingAPIView, IndexAPIView, MyCollectionAPIView, RecommendAPIView

urlpatterns = [
    path('index', IndexAPIView.as_view()),
    path('recommend', RecommendAPIView.as_view()),
    path('guessYouLike', GuessYouLikeAPIView.as_view()),
    path('iAmShooting', IAmShootingAPIView.as_view()),
    path('myCollection', MyCollectionAPIView.as_view()),
]
