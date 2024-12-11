from dsu.runtime.security.request_response import request_response
from dsu.dsu_gen.openapi.constants.config import PARSER_MAPPING
from dsu.dsu_gen.openapi.constants.config import RENDERER_MAPPING


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
    'REQUEST_QUERY_PARAMS_SERIALIZER': None,
    'REQUEST_HEADERS_SERIALIZER': None,
    'REQUEST_PATH_PARAMS_SERIALIZER': None,
    'DEFAULT_REQUEST_PATH_PARAMS': {},
    'REQUEST_SERIALIZER': None,
    'REQUEST_SERIALIZER_MANY_ITEMS': False,
    'RESPONSE': {
        
        '200': {
           'RESPONSE_SERIALIZER': None,
           'RESPONSE_SERIALIZER_MANY_ITEMS':  False,
           'HEADERS_SERIALIZER': None,
        }
        ,
        
        '400': {
           'RESPONSE_SERIALIZER': None,
           'RESPONSE_SERIALIZER_MANY_ITEMS':  False,
           'HEADERS_SERIALIZER': None,
        }
        ,
        
        '500': {
           'RESPONSE_SERIALIZER': None,
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

app_name = "edu_core"
operation_id  = "logout_user"
group_name = ""


@request_response(options=options, app_name=app_name, operation_id=operation_id, group_name=group_name)
def logout_user(request, *args, **kwargs):
    args = (request,) + args
    from dsu.dsu_gen.openapi.wrappers.view_env_wrapper import view_env_wrapper
    return view_env_wrapper(app_name, "logout_user", group_name, *args, **kwargs)
