from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.add_assignment_interactor import AddAssignmentInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    name=given_data.get('name')
    max_duration_in_minutes=given_data.get('max_duration_in_minutes')
    assignment_description=given_data.get('assignment_description')
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=AddAssignmentInteractor(storage=storage,presenter=presenter)
    data=interactor.add_assignment(name=name,max_duration_in_minutes=max_duration_in_minutes,assignment_description=assignment_description)
    return JsonResponse(data,status=200)