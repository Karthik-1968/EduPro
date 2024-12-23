from django.apps import AppConfig


class Type-formAppConfig(AppConfig):
    name = "type-form"

    def ready(self):
        from type-form import signals # pylint: disable=unused-variable
