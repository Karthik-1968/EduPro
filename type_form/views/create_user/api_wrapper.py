from dsu.dsu_gen.openapi.decorator.interface_decorator import validate_decorator
from .validator_class import ValidatorClass
from type_form.storages.storage_implementation import StorageImplementation
from type_form.presenters.presenter_implementation import PresenterImplementation
from type_form.interactors.create_user_interactor import CreateUserInteractor
from django.http import JsonResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    
    id=kwargs['request_data'].get('id')
    email = kwargs['request_data'].get('email')

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateUserInteractor(storage=storage)

    data = interactor.create_user(id=id,email=email,presenter=presenter)

    return JsonResponse(data,status=200)