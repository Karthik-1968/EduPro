from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.add_assignment_to_course_interactor import AddAssignmenttoCourseInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    course_id=given_data.get('course_id')
    assignment_id=given_data.get('assignment_id')

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=AddAssignmenttoCourseInteractor(storage=storage,presenter=presenter)

    data=interactor.add_assignment_to_course(course_id=course_id,assignment_id=assignment_id)
    
    return JsonResponse(data,status=200)