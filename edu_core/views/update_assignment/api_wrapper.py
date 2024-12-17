from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.update_assignment_interactor import UpdateAssignment

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    name=given_data.get('name')
    max_duration_in_minutes=given_data.get('max_duration_in_minutes')
    assignment_description=given_data.get('assignment_description')
    current_assignment=given_data.get('current_assignment')
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=UpdateAssignment(storage=storage,presenter=presenter)
    data=interactor.update_assignment(name=name,max_duration_in_mins=max_duration_in_minutes,assignment_description=assignment_description,current_assignment=current_assignment)
    return JsonResponse(data,status=200)
