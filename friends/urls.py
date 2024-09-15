from django.urls import path
from rest_framework import routers

from friends import views

app_name = 'friends'

urlpatterns = [
    path('list/', views.FriendsView.as_view(), name='friends')
]

router = routers.DefaultRouter()
router.register(r'api/friends', views.FriendsListView)
urlpatterns += router.urls
