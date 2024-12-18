from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import InvalidTeacher,MissingName,MissingEmail,MissingAge


class AddTeacherInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def add_teacher(self,name:str,email:str,age:int,presenter:PresenterInterface):
        """
        ELP:
            -validate input details
                -validate name
                -validate email
                -valiate age
            -check if teacher exists
            -add teacher
        """

        missing_input_fields=self.validate_input_data(name=name,email=email,age=age,presenter=presenter)
        if missing_input_fields:
            return missing_input_fields
        
        try:
            self.storage.valid_teacher(email=email)
        except InvalidTeacher:
            return presenter.raise_exception_for_invalid_teacher()
        
        teacher=self.storage.add_teacher(name=name,email=email,age=age)
        return presenter.get_add_teacher_response(teacher_id=teacher)
    
    def validate_input_data(self,name:str,email:str,age:int,presenter:PresenterInterface):
        try:
            self.storage.valid_name_field(name=name)
        except MissingName:
            return presenter.raise_exception_for_missing_name()

        try:
            self.storage.valid_email_field(email=email)
        except MissingEmail:
            return presenter.raise_exception_for_missing_email()
        
        try:
            self.storage.valid_age_field(age=age)
        except MissingAge:
            return presenter.raise_exception_for_missing_age()
        
        return None