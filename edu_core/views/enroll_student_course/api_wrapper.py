from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from edu_core.storages.storage_implementation import StorageImplementation
from edu_core.presenters.presenter_implementation import PresenterImplementation
from edu_core.interactors.enroll_student_course_interactor import EnrollStudentCourseInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    given_data=kwargs['request_data']
    course_id=given_data.get('course_id')
    teacher_id=given_data.get('student_id')
    user=kwargs['user']
    user_email=user.email
    
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=EnrollStudentCourseInteractor(storage=storage,presenter=presenter)

    data=interactor.enroll_student_course(student_id=teacher_id,course_id=course_id,user_email=user_email)

    return JsonResponse(data,status=200)
