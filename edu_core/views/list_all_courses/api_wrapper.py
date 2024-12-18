from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from edu_core.models import Teacher
from django.http import JsonResponse
from edu_core.models import Course
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.get_list_of_courses_interactor import ListofCoursesInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['query_params']
    l=given_data.get('limit')
    o=given_data.get('offset')
    search=given_data.get('search')
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=ListofCoursesInteractor(storage=storage,presenter=presenter)

    data=interactor.list_all_courses(limit=l,offset=o,search=search)
    
    return JsonResponse(data,safe=False,status=200)