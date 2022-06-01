from django.apps import AppConfig


class DjeotreeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "djeotree"

    def ready(self):
        import djeotree.signals  # noqa
