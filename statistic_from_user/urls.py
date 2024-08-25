from django.urls import path

from . import views

urlpatterns = [
    path('statistic/', views.StatisticView.as_view(), name='statistic')
]
