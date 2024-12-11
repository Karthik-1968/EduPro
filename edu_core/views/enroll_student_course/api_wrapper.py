from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from edu_core.models import Course
from edu_core.models import Student
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    try:
        course_id=given_data['course_id']
        student_id=given_data['student_id']
        try:
            course=Course.objects.get(id=course_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Course does not exist'}, status=404)
        try:
            student=Student.objects.get(id=student_id)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Student does not exist'}, status=404)
        return enroll_student_in_course(course,student)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
def enroll_student_in_course(course,student):
    name=student.name
    if course.student.filter(name=name).exists():
        return JsonResponse({"error": "Student is already enrolled in course."}, status=400)
    course.student.add(student)
    data={'course':course.name,'fee':course.fee,'duration':course.duration,'student':student.name}
    return JsonResponse(data,status=200)