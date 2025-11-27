from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class CrmConfig(AppConfig):
    name = 'koalixcrm.crm'

    def ready(self):
        from django.apps import apps
        from .listeners import register_log_signal_for_model
        
        logger.info("Starting to register NIS2 logging signals...")

        # We can explicitly list apps to check
        # to avoid scanning unnecessary third-party apps
        apps_to_scan = [
            'koalixcrm.crm', 
            'koalixcrm.accounting',
            'koalixcrm.subscriptions',
            'koalixcrm.djangoUserExtension'
            ]

        for app_name in apps_to_scan:
            try:
                app_config = apps.get_app_config(app_name.split('.')[-1])
                for model in app_config.get_models():
                    register_log_signal_for_model(model)
            except (LookupError, ImportError) as e:
                logger.warning(f"Could not register signals for app {app_name}: {e}")
        
        logger.info("Finished registering NIS2 logging signals.")
