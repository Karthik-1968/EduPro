from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.models import Submission,Student
from django.core.exceptions import ObjectDoesNotExist

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['query_params']
    try:
        id=given_data['search']
        user=kwargs['user']
        return grade_submission(id,user)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
def grade_submission(id,user):
    try:
        submission=Submission.objects.get(id=id)
        if user.email==submission.student.email:
            if submission.Grade:
                return JsonResponse({"error":"This submission is already graded"},status=400)
            submission.Grade='A'
            submission.remarks='Excellent'
            submission.save()
            return JsonResponse({"grade":submission.Grade},status=200)
        else:
            return JsonResponse({"Error":"User is not authorized"},status=403)
    except ObjectDoesNotExist:
            return JsonResponse({'error': 'Submission object does not exist'}, status=404)