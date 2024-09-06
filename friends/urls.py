from django.urls import path

from friends import views

app_name = 'friends'

urlpatterns = [
    path('list/', views.FriendsView.as_view(), name='friends')
]