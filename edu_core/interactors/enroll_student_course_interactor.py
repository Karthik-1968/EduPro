from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import MissingId,InvalidStudentId,InvalidCourseId,StudentAlreadyEnrolled,\
InvalidAccess

class EnrollStudentCourseInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage=storage
        self.presenter=presenter

    def enroll_student_course(self,student_id:int,course_id:int,user_email:str):
        """
        ELP:
            -validate input details
                -validate course_id
                -validate student_id
            check if student exists
            check if course exists
            check if user and student are same
            check if student already enrolled to course
            enroll student to course
        """
        missing_input_fields=self.validate_input_data(student_id=student_id,course_id=course_id)
        if missing_input_fields:
            return missing_input_fields
        
        input_not_exists=self.check_input_exists(student_id=student_id,course_id=course_id)
        if input_not_exists:
            return input_not_exists
        
        student=self.storage.get_student_details(id=student_id)

        try:
            email=student.email
            self.storage.check_user_authorization(email,user_email)
        except InvalidAccess:
            return self.presenter.raise_exception_for_invalid_access()

        try:
            self.storage.check_if_already_enrolled(student_id=student_id,course_id=course_id)
        except StudentAlreadyEnrolled:
            return self.presenter.raise_exception_for_student_already_enrolled()

        course_student_dtos=self.storage.enroll_student_course(student_id=student_id,course_id=course_id)
        return self.presenter.get_enroll_student_course_response(course_student_dtos=course_student_dtos)

    def validate_input_data(self,student_id:int,course_id:int):

        try:
            self.storage.validate_id(id=student_id)
        except MissingId:
            return self.presenter.raise_exception_for_missing_studentid()

        try:
            self.storage.validate_id(id=course_id)
        except MissingId:
            return self.presenter.raise_exception_for_missing_courseid()

        return None
    
    def check_input_exists(self,student_id:int,course_id:int):
        try:
            self.storage.check_student_exists(id=student_id)
        except InvalidStudentId:
            return self.presenter.raise_exception_for_invalid_student_id()

        try:
            self.storage.check_course_exists(id=course_id)
        except InvalidCourseId:
            return self.presenter.raise_exception_for_invalid_course_id()
        
        return None
