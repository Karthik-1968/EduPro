from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.models import Submission,Student
from django.core.exceptions import ObjectDoesNotExist

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    try:
        student=kwargs['request_data']['student']
        assignment=kwargs['request_data']['assignment']
        user=kwargs['user']
        stud=Student.objects.get(name=student)
        if user.email==stud.email:
            try:
                submission=Submission.objects.get(student__name=student,assignment__name=assignment)
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'Submission object does not exist'}, status=404)
            if submission.Grade:
                return JsonResponse({"error":"This submission is already graded"},status=400)
            submission.Grade='A'
            submission.remarks='Excellent'
            submission.save()
            return JsonResponse({"grade":submission.Grade},status=200)
        else:
            return JsonResponse({"Error":"User is not authorized"},status=403)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)