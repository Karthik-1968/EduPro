from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from edu_core.models import Assignment,Course
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    try:
        course_id=given_data['course_id']
        assignment_id=given_data['assignment_id']
        try:
            course=Course.objects.get(id=course_id)
        except ObjectDoesNotExist:
            return JsonResponse({"Error": "Course does not exist."},status=404)
        try:
            assignment=Assignment.objects.get(id=assignment_id)
        except ObjectDoesNotExist:
            return JsonResponse({"Error": "Assignment does not exist."},status=404)
        return add_assignment_course(course,assignment,assignment_id)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
def add_assignment_course(course,assignment,assignment_id):
    if course.assignment_set.filter(id=assignment_id).exists():
        return JsonResponse({"error": "Assignment is already added to course."}, status=400)
    assignment.course=course
    assignment.save()
    data={
        'course':course.name,'assignment':assignment.name,'max_duration_in_minutes': assignment.max_duration, 'assignment_description': assignment.assign_description
    }
    return JsonResponse(data,status=200)