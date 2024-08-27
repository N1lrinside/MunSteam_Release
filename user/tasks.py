from celery import shared_task

from .service import get_fullinfo_user


@shared_task
def update_info(steam_id):
    get_fullinfo_user(steam_id)