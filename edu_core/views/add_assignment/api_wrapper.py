from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.models import Assignment

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    try:
        name=given_data['name']
        duration=given_data['max_duration_in_minutes']
        description=given_data['assignment_description']
        return add_assignment(name,description,duration)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
def add_assignment(name,description,duration):
    if Assignment.objects.filter(name=name).exists():
        return JsonResponse({"error":"assignment already present"},status=400)
    assignment=Assignment.objects.create(name=name,max_duration=duration,assign_description=description)
    return {"id":assignment.id}