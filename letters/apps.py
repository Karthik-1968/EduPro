from django.apps import AppConfig


class LettersAppConfig(AppConfig):
    name = "letters"

    def ready(self):
        from letters import signals # pylint: disable=unused-variable
