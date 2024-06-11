from django.apps import AppConfig
import logging


class HomeCareServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home_care_services'
 
    def ready(self):
        import home_care_services.signals
        logging.info("Signals module imported in YourAppConfig.ready()")
