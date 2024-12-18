from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.exceptions.custom_exceptions import MissingId,MissingSubmittedAt,InvalidStudentId,InvalidAssignmentId,\
InvalidAccess,AssignmentAlreadySubmitted

class AddSubmissionInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage=storage
        self.presenter=presenter

    def add_submission(self,student_id:int,assignment_id:int,submitted_at:str,user_email:str):
        """
        ELP:
            -validating input
                -validate student_id
                -validate assignment_id
                -validate submitted_at
            -check if assignment exists
            -check if student exists
            -check if student and user are same
            -check if student already submitted the assignment
            -submit the assignment
        """
        missing_input_fields=self.validate_input_fields(student_id=student_id,assignment_id=assignment_id,submitted_at=submitted_at)
        if missing_input_fields:
            return missing_input_fields
        
        input_not_exists=self.check_input_exists(student_id=student_id,assignment_id=assignment_id)
        if input_not_exists:
            return input_not_exists
        
        student=self.storage.get_student_details(id=student_id)

        try:
            student_email=student.email
            self.storage.check_user_authorization(email=student_email,user_email=user_email)
        except InvalidAccess:
            return self.presenter.raise_exception_for_invalid_access()
        
        try:
            self.storage.check_if_already_submitted(student_id=student_id,assignment_id=assignment_id)
        except AssignmentAlreadySubmitted:
            return self.presenter.raise_exception_for_assignment_already_submitted()
        
        submission_id=self.storage.add_submission(student_id=student_id,assignment_id=assignment_id,submitted_at=submitted_at)
        return self.presenter.get_add_submission_response(submission_id=submission_id)

    def validate_input_fields(self,student_id:int,assignment_id:int,submitted_at:str):

        try:
            self.storage.validate_id(id=student_id)
        except MissingId:
            return self.presenter.raise_exception_for_missing_studentid()
        
        try:
            self.storage.validate_id(id=assignment_id)
        except MissingId:
            return self.presenter.raise_exception_for_missing_assignmentid()
        
        try:
            self.storage.validate_submitted_at(submitted_at=submitted_at)
        except MissingSubmittedAt:
            return self.presenter.raise_exception_for_missing_submittedat()
        
        return None
    
    def check_input_exists(self,student_id:int,assignment_id:int):

        try:
            self.storage.check_student_exists(id=student_id)
        except InvalidStudentId:
            return self.presenter.raise_exception_for_invalid_student_id()
        
        try:
            self.storage.check_assignment_exists(id=assignment_id)
        except InvalidAssignmentId:
            return self.presenter.raise_exception_for_invalid_assignment_id()
        
        return None