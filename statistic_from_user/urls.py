from django.urls import path
from rest_framework import routers

from . import views

urlpatterns = [
    path('', views.ChoiseView.as_view(), name='statistic'),
    path('ur/', views.YourStatisticView.as_view(), name='statistic_ur'),
    path('with_friends/', views.StatisticWithFriendsView.as_view(), name='statistic_with_friend'),
]

router = routers.DefaultRouter()
router.register(r'api/user_statistic', views.StatisticView)
urlpatterns += router.urls
