from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from edu_core.models import Submission
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['query_params']
    try:
        id=given_data["search"]
        l=given_data['limit']
        o=given_data['offset']
        submissions_of_assignment(id,l,o)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
def submissions_of_assignment(id,l,o):
    try:
        submissions=Submission.objects.filter(assignment_id=id)[o:o+l]
    except ObjectDoesNotExist:
            return JsonResponse({'error': 'submission does not exist'}, status=404)
    data=[{'submitted_by':submission.student.name,'submitted_at':submission.submitted_at,'Grade':submission.Grade,'remarks':submission.remarks} for submission in submissions]
    return JsonResponse(data,safe=False,status=200) 