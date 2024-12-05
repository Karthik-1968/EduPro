from django.apps import AppConfig

class EduCoreAppConfig(AppConfig):
    name = "edu_core"

    def ready(self):
        from edu_core import signals # pylint: disable=unused-variable
