from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.models import Course
from django.db import IntegrityError

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    try:
        name=given_data['name']
        fee=given_data['fee']
        duration=given_data['duration']
        data=add_course(name,fee,duration)
        return JsonResponse(data,status=200)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
def add_course(name,fee,duration):
    if Course.name:
        return JsonResponse({"error": "Course is already created."}, status=400)
    course=Course.objects.create(name=name,fee=fee,duration=duration)
    data={"id":course.id}
    return data