from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.exceptions.custom_exceptions import InvalidStudentId,InvalidAccess,MissingId

class DeleteStudent:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def delete_student(self,student_id:int,user_email:str,presenter:PresenterInterface):

        """
        ELP:
            -validate input
                -validate id
            -if student present
                -if student and user same
                    -delete student
                -else error
            -else error
        """
        try:
            self.storage.validate_id(id=student_id)
        except MissingId:
            return presenter.raise_exception_for_missingid()
        
        try:
            self.storage.check_student_exists(id=student_id)
        except InvalidStudentId:
            return presenter.raise_exception_for_invalid_student_id()
        
        student=self.storage.get_student_details(id=student_id)

        try:
            email=student.email
            self.storage.check_user_authorization(email,user_email)
        except InvalidAccess:
            return presenter.raise_exception_for_invalid_access()
        
        self.storage.delete_student(id=student_id)
        return presenter.get_delete_student_response()
