from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from edu_core.models import Student
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.get_list_of_students_interactor import ListofStudents


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['query_params']
    l=given_data.get('limit')
    o=given_data.get('offset')
    search=given_data.get('search')
    presenter=PresenterImplementation()
    storage=StorageImplementation()
    interactor=ListofStudents(storage=storage)
    data=interactor.list_of_students(limit=l,offset=o,search=search,presenter=presenter)
    return JsonResponse(data,safe=False,status=200)