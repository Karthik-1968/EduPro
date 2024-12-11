from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from edu_core.models import Course
from edu_core.models import Teacher
from django.http import JsonResponse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    try:
        course_id=given_data['course_id']
        teacher_id=given_data['teacher_id']
        try:
            course=Course.objects.get(id=course_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Course does not exist'}, status=404)
        try:
            teacher=Teacher.objects.get(id=teacher_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Teacher does not exist'}, status=404)
        assign_teacher_to_course(course,teacher)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
def assign_teacher_to_course(course,teacher):
    if course.teacher:
        return JsonResponse({"error": "Teacher is already assigned to course."}, status=400)
    course.teacher.add(teacher)
    data={'course':course.name,'fee':course.fee,'duration':course.duration,'teacher':teacher.name}
    return JsonResponse(data,status=200)
