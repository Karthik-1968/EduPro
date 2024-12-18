from dsu.dsu_gen.openapi.decorator.interface_decorator import validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.create_login_interactor import LoginInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_email = kwargs['request_data'].get('user_email')

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=LoginInteractor(storage=storage)
    
    data=interactor.login(user_email=user_email,presenter=presenter)

    return JsonResponse(data, status=200)