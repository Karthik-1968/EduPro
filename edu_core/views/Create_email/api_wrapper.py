from django.db import IntegrityError
from dsu.dsu_gen.openapi.decorator.interface_decorator import validate_decorator
from .validator_class import ValidatorClass
from edu_core.models import User
from django.http import JsonResponse

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    email = kwargs['request_data']['email']
    email_not_present=not email
    if email_not_present:
        return JsonResponse({"error": "Search parameter is missing"}, status=400)
    try:
        User.objects.create(user_id="7ca96872-023b-4629-ac94-5b3ccc2b4feb",email=email)
        return JsonResponse({"Success":"User is successfully created"},status=200)
    except IntegrityError as e:
        return JsonResponse({"error":"unique constraint is failed for email"},status=400)