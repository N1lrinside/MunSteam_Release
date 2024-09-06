from django.urls import path

from . import views

urlpatterns = [
    path('statistic/', views.ChoiseView.as_view(), name='statistic'),
    path('statistic/ur/', views.YourStatisticView.as_view(), name='statistic_ur'),
    path('statistic/with_friends', views.StatisticWithFriendsView.as_view(), name='statistic_with_friend'),
]
