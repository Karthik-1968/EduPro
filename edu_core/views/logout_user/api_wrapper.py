from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from ib_users.interfaces.service_interface import ServiceInterface
from django.http import JsonResponse

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    try:
        user=kwargs['user']
        user_id=user.user_id
        service_interface = ServiceInterface()
        service_interface.logout_in_all_devices(user_id)
        return JsonResponse({"message": "Successfully logged out from all devices."}, status=200)
    except Exception as e:
        return JsonResponse({"error": f"Failed to log out: {str(e)}"},status=500)