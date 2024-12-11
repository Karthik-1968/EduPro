from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from edu_core.models import Teacher
from django.http import JsonResponse
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
                teacher=Teacher.objects.get(id=id)
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'teacher does not exist'}, status=404)
            data={'name':teacher.name,'email':teacher.email,'age':teacher.age}
            return JsonResponse(data,status=200)
        else:
            try:
                teachers=Teacher.objects.all()[o:o+l]
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'teacher does not exist'}, status=404)
            data = [{'name': teacher.name, 'email': teacher.email, 'age': teacher.age} for teacher in teachers]
            return JsonResponse(data,safe=False,status=200)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)