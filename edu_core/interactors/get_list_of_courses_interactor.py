from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import InvalidCourseId


class ListofCoursesInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage=storage
        self.presenter=presenter

    def list_all_courses(self,limit:int,offset:int,search:int)->list[dict]:
        """
        ELP:
            -if search
                -if course exists
                -else error
                -get course_details
            -else
                -get list of course details
        """
        if search:
            try:
                self.storage.check_course_exists(id=search)
            except InvalidCourseId:
                self.presenter.raise_exception_for_invalid_course_id()
            
            course_dto=self.storage.get_course_details(id=search)
            return self.presenter.get_course_details_response(course_dto=course_dto)
        else:
            course_dtos=self.storage.get_list_of_courses_details(limit=limit,offset=offset)
            return self.presenter.get_list_of_courses_details_response(course_dtos=course_dtos)
