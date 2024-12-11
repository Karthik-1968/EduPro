from dsu.dsu_gen.openapi.decorator.interface_decorator import validate_decorator
from .validator_class import ValidatorClass
from edu_core.models import Student
from django.http import JsonResponse

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    try:
        name = given_data['name']
        email = given_data['email']
        age = given_data['age']
        if Student.objects.filter(name=name).exists():
            return JsonResponse({"error": "Student is already created."}, status=400)
        data=add_student(name,email,age)
        return JsonResponse(data, status=200)
    except KeyError as e:
        return JsonResponse({"error": f"Missing parameter: {e}"}, status=400)
def add_student(name,email,age):
    student=Student.objects.create(name=name, email=email, age=age)
    data={"id":student.id}
    return data