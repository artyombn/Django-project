from django.apps import AppConfig


class PartnershipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'partnership'

    def ready(self):
        import partnership.signals


