from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import InvalidStudent,MissingName,MissingEmail,MissingAge

class AddStudentInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def add_student(self,name:str,email:str,age:int,presenter:PresenterInterface):
        """
        ELP:
        - Validate input
            - validate name
            - validate email
            - validate age
        - check if student exists
            - if yes:
                return student
            - else:
                create a student

        """
        validation_data=self.validate_input_data(name=name,email=email,age=age,presenter=presenter)
        if validation_data:
            return validation_data

        try:
            self.storage.valid_student(email=email)
        except InvalidStudent:
            return presenter.raise_exception_for_invalid_student()
        
        student=self.storage.add_student(name=name,email=email,age=age)
        return presenter.get_add_student_response(student_id=student)
    
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
