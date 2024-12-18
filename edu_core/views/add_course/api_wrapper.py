from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.add_course_interactor import AddCourseInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    name=given_data.get('name')
    fee=given_data.get('fee')
    duration=given_data.get('duration')
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=AddCourseInteractor(storage=storage,presenter=presenter)

    data=interactor.add_course(name=name,fee=fee,duration=duration)
    
    return JsonResponse(data,status=200)