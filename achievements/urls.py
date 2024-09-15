from django.urls import path
from rest_framework import routers

from achievements import views

urlpatterns = [
    path('', views.GameAchievementView.as_view(), name='achievements_games'),
    path('<int:app_id>', views.AchievementsView.as_view(), name='achievements')
]

router = routers.DefaultRouter()
router.register(r'api/achievements/gamesuser', views.GamesUserView)
router.register(r'api/achievements/achievementsgame', views.AchievementsUserView)
urlpatterns += router.urls
