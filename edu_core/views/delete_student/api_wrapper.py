from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.delete_student_interactor import DeleteStudent

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user=kwargs['user']
    id=kwargs['query_params'].get('search')
    user_email=user.email
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=DeleteStudent(storage=storage)
    data=interactor.delete_student(student_id=id,user_email=user_email,presenter=presenter)
    return JsonResponse(data,status=200)

