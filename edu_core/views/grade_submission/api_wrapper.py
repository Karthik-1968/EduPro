from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.grade_submission_interactor import GradeSubmission

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['query_params']
    id=given_data.get('search')
    user=kwargs['user']
    user_email=user.email
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=GradeSubmission(storage=storage,presenter=presenter)
    data=interactor.grade_submission(submission_id=id,user_email=user_email)
    return JsonResponse(data,status=200)


