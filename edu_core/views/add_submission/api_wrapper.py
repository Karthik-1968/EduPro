from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.models import Submission,Student,Assignment
from django.core.exceptions import ObjectDoesNotExist

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    try:
        assignment_id=given_data['assignment_id']
        student_id=given_data['student_id']
        submitted_at=given_data['submitted_at']
        user=kwargs['user']
        return add_submission(assignment_id,student_id,submitted_at,user)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
def add_submission(assignment_id,student_id,submitted_at,user):
    try:
        student=Student.objects.get(id=student_id)
    except ObjectDoesNotExist:
        return JsonResponse({"Error":"Student doesn't exist"},status=404)
    try:
        assignment=Assignment.objects.get(id=assignment_id)
    except ObjectDoesNotExist:
        return JsonResponse({"Error":"Student doesn't exist"},status=404)
    if user.email==student.email:
        if Submission.objects.filter(assignment=assignment,student=student).exists():
            return JsonResponse({"Error": "Assignment is already submitted."}, status=400)
        submission=Submission.objects.create(assignment=assignment,student=student,submitted_at=submitted_at)
        return JsonResponse({"id":submission.id},status=200)
    else:
        return JsonResponse({"Error":"User is not authorized"},status=403)