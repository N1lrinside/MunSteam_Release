from celery import shared_task

from .service import update_info_user


@shared_task
def update_info(steam_id):
    update_info_user(steam_id)