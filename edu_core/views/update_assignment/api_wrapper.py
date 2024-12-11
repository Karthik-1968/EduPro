from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.models import Assignment
from django.core.exceptions import ObjectDoesNotExist

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    try:
        name=given_data['name']
        max_duration_in_minutes=given_data['max_duration_in_minutes']
        assignment_description=given_data['assignment_description']
        current_assignment=given_data['current_assignment']
        return update_assignment(name,max_duration_in_minutes,assignment_description,current_assignment)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
def update_assignment(name,max_duration_in_minutes,assignment_description,current_assignment):
    try:
        assignment=Assignment.objects.get(id=current_assignment)
    except ObjectDoesNotExist:
            return JsonResponse({'error': 'Object does not exist'}, status=404)
    assignment.name=name
    assignment.max_duration=max_duration_in_minutes
    assignment.assign_description=assignment_description
    assignment.save()
    data={
        'name':assignment.name,
        'max_duration_in_minutes':assignment.max_duration,
        'assignment_description':assignment.assign_description
    }
    return JsonResponse(data,status=200)    
