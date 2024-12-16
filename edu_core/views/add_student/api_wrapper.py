from dsu.dsu_gen.openapi.decorator.interface_decorator import validate_decorator
from edu_core.interactors.add_student_interactor import AddStudentInteractor
from .validator_class import ValidatorClass
from edu_core.models import Student
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    name = given_data.get("name")
    email = given_data.get("email")
    age = given_data.get("age")
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=AddStudentInteractor(storage=storage)

    data=interactor.add_student(name=name,email=email,age=age,presenter=presenter)

    return JsonResponse(data, status=200)