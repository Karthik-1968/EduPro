from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.exceptions.custom_exceptions import MissingId,InvalidCourseId


class AssignmentsofCourseInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage=storage
        self.presenter=presenter

    def assignments_of_course(self,limit:int,offset:int,id:int):
        """
        ELP:
            -validate input
                -validate id
            -check if course exists
            -get assignmets of course
        """
        try:
            self.storage.validate_id(id=id)
        except MissingId:
            self.presenter.raise_exception_for_missing_courseid()
        
        try:
            self.storage.check_course_exists(id=id)
        except InvalidCourseId:
            self.presenter.raise_exception_for_invalid_course_id()
        
        assignment_dtos=self.storage.assignments_of_course(limit=limit,offset=offset,id=id)
        return self.presenter.get_assignments_of_course_response(assignment_dtos=assignment_dtos)