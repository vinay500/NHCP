from django.apps import AppConfig

class BeyondBordersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'beyond_borders'

    def ready(self):
        import beyond_borders.signals
