from dsu.dsu_gen.openapi.decorator.interface_decorator import validate_decorator
from .validator_class import ValidatorClass
from ib_users.interfaces.service_interface import ServiceInterface
from rest_framework.response import Response
from django.http import JsonResponse
from edu_core.models import User
from django.core.exceptions import ObjectDoesNotExist

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    try:
        user_email = kwargs['request_data'].get('user_email')
        try:
            user = User.objects.get(email=user_email).user_id
        except ObjectDoesNotExist:
            return JsonResponse({'error': f'User with email {user_email} does not exist'}, status=404)
        data=login(user)
        return JsonResponse(data, status=200)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
def login(user):
    service_interface = ServiceInterface()
    auth_tokens = service_interface.create_auth_tokens_for_user(user)
    data = {
        "access_token": auth_tokens.access_token,
        "expires_in": auth_tokens.expires_in
    }
    return data