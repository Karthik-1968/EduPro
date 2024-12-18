from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.delete_assignment_interactor import DeleteAssignmentInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    id=kwargs['query_params'].get('search')
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=DeleteAssignmentInteractor(storage=storage)

    data=interactor.delete_assignment(assignment_id=id,presenter=presenter)
    
    return JsonResponse(data,status=200)