from celery import shared_task

from .service import player_count, get_time


@shared_task
def get_players_in_game():
    player_count()


@shared_task
def update_time():
    get_time()
