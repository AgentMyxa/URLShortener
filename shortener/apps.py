from django.apps import AppConfig
from .service import storage
from . import scheduler

class ShortenerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shortener'


    def ready(self):
        storage.init()
        #scheduler.start()