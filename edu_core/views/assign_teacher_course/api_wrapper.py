from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.assign_teacher_course_interactor import AssignTeacherCourseInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    course_id=given_data.get('course_id')
    teacher_id=given_data.get('teacher_id')
    user=kwargs['user']
    user_email=user.email
    
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=AssignTeacherCourseInteractor(storage=storage,presenter=presenter)

    data=interactor.assign_teacher_course(teacher_id=teacher_id,course_id=course_id,user_email=user_email)

    return JsonResponse(data,status=200)
