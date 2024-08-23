from django.urls import path

from achievements import views

urlpatterns = [
    path('achievements/', views.GameAchievementView.as_view(), name='achievements_games'),
    path('achievements/<int:app_id>', views.AchievementsView.as_view(), name='achievements')
]