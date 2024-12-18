from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import MissingId,InvalidTeacherId,InvalidCourseId,TeacherAlreadyAssigned,\
InvalidAccess


class AssignTeacherCourseInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage=storage
        self.presenter=presenter

    def assign_teacher_course(self,teacher_id:int,course_id:int,user_email:str):
        """
        ELP:
            -validate input details
                -validate course_id
                -validate teacher_id
            check if teacher exists
            check if course exists
            check if user and teacher are same
            check if teacher already assigned to course
            assign teacher to course
        """
        missing_input_fields=self.validate_input_data(teacher_id=teacher_id,course_id=course_id)
        if missing_input_fields:
            return missing_input_fields
        
        input_not_exists=self.check_input_exists(teacher_id=teacher_id,course_id=course_id)
        if input_not_exists:
            return input_not_exists
        
        teacher=self.storage.get_teacher_details(id=teacher_id)
        
        try:
            email=teacher.email
            self.storage.check_user_authorization(email,user_email)
        except InvalidAccess:
            return self.presenter.raise_exception_for_invalid_access()

        try:
            self.storage.check_if_already_assigned(teacher_id=teacher_id,course_id=course_id)
        except TeacherAlreadyAssigned:
            return self.presenter.raise_exception_for_teacher_already_assigned()

        course_teacher_dtos=self.storage.assign_teacher_course(teacher_id=teacher_id,course_id=course_id)
        return self.presenter.get_assign_teacher_course_response(course_teacher_dtos=course_teacher_dtos)

    def validate_input_data(self,teacher_id:int,course_id:int):

        try:
            self.storage.validate_id(id=teacher_id)
        except MissingId:
            return self.presenter.raise_exception_for_missing_teacherid()

        try:
            self.storage.validate_id(id=course_id)
        except MissingId:
            return self.presenter.raise_exception_for_missing_courseid()

        return None
    
    def check_input_exists(self,teacher_id:int,course_id:int):

        try:
            self.storage.check_teacher_exists(id=teacher_id)
        except InvalidTeacherId:
            return self.presenter.raise_exception_for_invalid_teacher_id()

        try:
            self.storage.check_course_exists(id=course_id)
        except InvalidCourseId:
            return self.presenter.raise_exception_for_invalid_course_id()
        
        return None