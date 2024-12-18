from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.exceptions.custom_exceptions import MissingId,InvalidAssignmentId,InvalidCourseId,\
AssignmentAlreadyAddedtoCourse


class AddAssignmenttoCourse:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage=storage
        self.presenter=presenter

    def add_assignment_to_course(self,assignment_id:int,course_id:int):
        """
        ELP:
            -check if course exists
            -check if teacher exists
            -check if assignment is already added to  course
            -add assignment to course
        """
        check_if_input_exists=self.check_input_exists(course_id=course_id,assignment_id=assignment_id)
        if check_if_input_exists:
            return check_if_input_exists
        
        try:
            self.storage.check_if_assignment_already_added_to_course(course_id=course_id,assignment_id=assignment_id)
        except AssignmentAlreadyAddedtoCourse:
            return self.presenter.raise_exception_for_assignment_already_added_to_course()
        
        course_assignment_dtos=self.storage.add_assignment_to_course(course_id=course_id,assignment_id=assignment_id)
        return self.presenter.get_add_assignment_to_course_response(course_assignment_dtos=course_assignment_dtos)
    
    def check_input_exists(self,course_id:int,assignment_id:int):

        try:
            self.storage.check_course_exists(id=course_id)
        except InvalidCourseId:
            return self.presenter.raise_exception_for_invalid_course_id()
        
        try:
            self.storage.check_assignment_exists(id=assignment_id)
        except InvalidAssignmentId:
            return self.presenter.raise_exception_for_invalid_assignment_id()
        
        return None
    

        
