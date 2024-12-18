from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.exceptions.custom_exceptions import InvalidTeacherId,InvalidAccess,MissingId


class DeleteTeacherInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def delete_teacher(self,teacher_id:int,user_email:str,presenter:PresenterInterface):

        """
        ELP:
            -validate input
                -validate id
                
            -if teacher present
            -else error

            -if teacher and user same
            -else error

            -delete teacher
        """
        try:
            self.storage.validate_id(id=teacher_id)
        except MissingId:
            presenter.raise_exception_for_missingid()
        
        try:
            self.storage.check_teacher_exists(id=teacher_id)
        except InvalidTeacherId:
            presenter.raise_exception_for_invalid_teacher_id()
        
        teacher=self.storage.get_teacher_details(id=teacher_id)

        try:
            email=teacher.email
            self.storage.check_user_authorization(email,user_email)
        except InvalidAccess:
            presenter.raise_exception_for_invalid_access()
        
        self.storage.delete_teacher(id=teacher_id)
        return presenter.get_delete_teacher_response()
