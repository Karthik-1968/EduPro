from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.models import Assignment
from django.core.exceptions import ObjectDoesNotExist

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    try:
        id=kwargs['query_params']['search']
        try:
            assignment=Assignment.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'assignment does not exist'}, status=404)
        assignment.delete()
        return JsonResponse({"Sucess":"Successfully deleted"},status=200)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)