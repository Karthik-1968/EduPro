from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.add_submission_interactor import AddSubmissionInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    assignment_id=given_data.get('assignment_id')
    student_id=given_data.get('student_id')
    submitted_at=given_data.get('submitted_at')
    user=kwargs['user']
    user_email=user.email

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=AddSubmissionInteractor(storage=storage,presenter=presenter)

    data=interactor.add_submission(student_id=student_id,assignment_id=assignment_id,submitted_at=submitted_at,\
                                   user_email=user_email)
    
    return JsonResponse(data,status=200)