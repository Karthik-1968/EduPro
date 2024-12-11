from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.models import Assignment
from django.core.exceptions import ObjectDoesNotExist

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['query_params']
    try:
        l=given_data['limit']
        o=given_data['offset']
        id=given_data['search']
        return assignments_of_course(l,o,id)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
def assignments_of_course(l,o,id):
    assignments=Assignment.objects.filter(course_id=id)
    if assignments:
        assignments=assignments[o:o+l]
        data=[{"assignment_name":assignment.name} for assignment in assignments]
        return JsonResponse(data,safe=False,status=200)
    else:
        return JsonResponse({"error":"Assignments doesn't exist"},status=404)