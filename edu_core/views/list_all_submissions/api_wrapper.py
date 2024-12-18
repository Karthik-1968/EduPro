from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.get_list_of_submissions_of_assignment_interactor import ListofSubmissions


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['query_params']
    id=given_data.get("search")
    l=given_data.get('limit')
    o=given_data.get('offset')
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=ListofSubmissions(storage=storage,presenter=presenter)
    data=interactor.list_of_submissions(limit=l,offset=o,id=id)
    return JsonResponse(data,safe=False,status=200)
