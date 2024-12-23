from dsu.runtime.security.request_response import request_response
from dsu.dsu_gen.openapi.constants.config import PARSER_MAPPING
from dsu.dsu_gen.openapi.constants.config import RENDERER_MAPPING
from type_form.build.view_environments.add_fields_to_form_.add_fields_to_form.AddFieldsToFormRequestQueryParamSerializer import AddFieldsToFormRequestQueryParamSerializer
from type_form.build.view_environments.add_fields_to_form_.add_fields_to_form.responses.Status_201.Status_201.Status_201Serializer import Status_201Serializer


options = {
    'METHOD': 'POST',
    'REQUEST_WRAPPING_REQUIRED': False,
    'REQUEST_ENCRYPTION_REQUIRED': False,
    'REQUEST_IS_PARTIAL': False,
    'PARSER_CLASSES': [
        PARSER_MAPPING["application/json"]
    ],
    'RENDERER_CLASSES': [
        RENDERER_MAPPING["application/json"]
    ],
    'REQUEST_QUERY_PARAMS_SERIALIZER': AddFieldsToFormRequestQueryParamSerializer,
    'REQUEST_HEADERS_SERIALIZER': None,
    'REQUEST_PATH_PARAMS_SERIALIZER': None,
    'DEFAULT_REQUEST_PATH_PARAMS': {},
    'REQUEST_SERIALIZER': None,
    'REQUEST_SERIALIZER_MANY_ITEMS': False,
    'RESPONSE': {
        
        '201': {
           'RESPONSE_SERIALIZER': Status_201Serializer,
           'RESPONSE_SERIALIZER_MANY_ITEMS':  False,
           'HEADERS_SERIALIZER': None,
        }
        
    },
    "SECURITY": {

        "oauth" : [
            "write"
            
        ]
    },
    'LOG_CONFIG': {'request_log_selector': 'ENABLE_COMPLETE_LOG', 'response_log_selector': 'ENABLE_COMPLETE_LOG'}
}

app_name = "type_form"
operation_id  = "add_fields_to_form"
group_name = ""


@request_response(options=options, app_name=app_name, operation_id=operation_id, group_name=group_name)
def add_fields_to_form(request, *args, **kwargs):
    args = (request,) + args
    from dsu.dsu_gen.openapi.wrappers.view_env_wrapper import view_env_wrapper
    return view_env_wrapper(app_name, "add_fields_to_form", group_name, *args, **kwargs)
