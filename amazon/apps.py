from django.apps import AppConfig


class AmazonAppConfig(AppConfig):
    name = "amazon"

    def ready(self):
        from amazon import signals # pylint: disable=unused-variable
