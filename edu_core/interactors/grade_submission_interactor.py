from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.exceptions.custom_exceptions import MissingId,InvalidSubmissionId,InvalidAccess,SubmissionAlreadyGraded


class GradeSubmission:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage=storage
        self.presenter=presenter

    def grade_submission(self,submission_id:int,user_email:str):
        """
        ELP:
            -validate input details
                -validate id
            -check if submission exists
            -check if user is teacher
            -check if submission is already graded
            -grade the submission
        """
        try:
            self.storage.validate_id(id=submission_id)
        except MissingId:
            return self.presenter.raise_exception_for_missing_submissionid()
        
        try:
            self.storage.check_submission_exists(id=submission_id)
        except InvalidSubmissionId:
            return self.presenter.raise_exception_for_invalid_submission_id()

        try:
            self.storage.check_user_is_teacher(user_email=user_email)
        except InvalidAccess:
            return self.presenter.raise_exception_for_invalid_access()

        try:
            self.storage.check_if_submission_already_graded(id=submission_id)
        except SubmissionAlreadyGraded:
            return self.presenter.raise_exception_for_submission_already_graded()
        
        
        grade=self.storage.grade_submission(id=submission_id)
        return self.presenter.get_grade_submission_response(grade=grade)
    
