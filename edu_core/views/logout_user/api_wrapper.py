from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.create_logout_interactor import Logout

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user=kwargs['user']
    user_id=user.user_id
    presenter=PresenterImplementation()
    interactor=Logout(presenter=presenter)
    data=interactor.logout(user_id=user_id)
    return JsonResponse(data,status=200)
    