from dsu.dsu_gen.openapi.constants.config import PARSER_MAPPING
from dsu.dsu_gen.openapi.constants.config import RENDERER_MAPPING

from django.conf import settings
django_swagger_utils_settings = settings.SWAGGER_UTILS
defaults = django_swagger_utils_settings["DEFAULTS"]


REQUEST_RESPONSE_DECORATOR = {
    'METHOD': 'POST',
    'REQUEST_WRAPPING_REQUIRED': defaults.get("REQUEST_WRAPPING_REQUIRED", True),
    'REQUEST_ENCRYPTION_REQUIRED': defaults.get("REQUEST_ENCRYPTION_REQUIRED", False),
    'REQUEST_IS_PARTIAL': False,
    'REQUEST_SERIALIZER_MANY_ITEMS': False,
    'RESPONSE_SERIALIZER_MANY_ITEMS': False,
    'PARSER_CLASSES': [
        PARSER_MAPPING["application/json"]
    ],
    'RENDERER_CLASSES': [
        RENDERER_MAPPING["application/json"]
    ],
    "SECURITY": {

    },
    'REQUEST_SERIALIZER': None,
    'RESPONSE': {
        '200': {
            'CONTENT_TYPE': "application/json",
            'RESPONSE_SERIALIZER': None,
            'HEADERS_SERIALIZER': None,
        }
    }
}