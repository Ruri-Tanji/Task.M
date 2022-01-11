from django.apps import AppConfig


class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'

class MemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'memo'
