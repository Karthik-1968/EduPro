from django.db import IntegrityError
from dsu.dsu_gen.openapi.decorator.interface_decorator import validate_decorator
from .validator_class import ValidatorClass
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.create_user_interactor import CreateUserInteractor
from django.http import JsonResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    
    email = kwargs['request_data'].get('email')

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=CreateUserInteractor(storage=storage)

    data=interactor.create_user(email=email,presenter=presenter)

    return JsonResponse(data,status=200)