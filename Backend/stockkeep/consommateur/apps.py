from django.apps import AppConfig


class ConsommateurConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'consommateur'
    def ready(self):
        import consommateur.signals