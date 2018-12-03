from django.urls import path

from msg.views import MsgAPIView, MsgDetailAPIView

urlpatterns = [
    path('list', MsgAPIView.as_view()),
    path('detail', MsgDetailAPIView.as_view()),
]
