from django.apps import AppConfig


class TypeFormAppConfig(AppConfig):
    name = "type_form"

    def ready(self):
        from type_form import signals # pylint: disable=unused-variable
