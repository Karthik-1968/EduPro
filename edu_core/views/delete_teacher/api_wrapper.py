from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.models import Teacher
from django.core.exceptions import ObjectDoesNotExist

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    try:
        user=kwargs['user']
        id=kwargs['query_params']['search']
        return delete_teacher(user,id)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
def delete_teacher(user,id):
    try:
        teacher=Teacher.objects.get(id=id)
        if user.email==teacher.email:
            teacher.delete()
            return JsonResponse({"Sucess":"Successfully deleted"},status=200)
        else:
            return JsonResponse({"Error":"User is not authorized"},status=403)
    except ObjectDoesNotExist:
            return JsonResponse({"Error":"Teacher does not exist"}, status=404)