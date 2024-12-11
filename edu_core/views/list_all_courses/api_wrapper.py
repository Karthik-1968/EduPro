from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from edu_core.models import Teacher
from django.http import JsonResponse
from edu_core.models import Course
from django.core.exceptions import ObjectDoesNotExist

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['query_params']
    try:
        l=given_data['limit']
        o=given_data['offset']
        if given_data['search']:
            id=given_data['search']
            try:
                course=Course.objects.get(id=id)
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'course does not exist'}, status=404)
            data={'name':course.name,'fee':course.fee,'duration':course.duration}
            return JsonResponse(data,status=200)
        else:
            try:
                courses=Course.objects.all()[o:o+l]
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Object does not exist'}, status=404)
            data=[{'name':course.name,'fee':course.fee,'duration':course.duration} for course in courses]
            return JsonResponse(data,safe=False,status=200)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)