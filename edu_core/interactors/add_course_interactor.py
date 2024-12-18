from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import MissingName,MissingFee,MissingDuration,InvalidCourse


class AddCourseInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage=storage
        self.presenter=presenter
    
    def add_course(self,name:str,fee:int,duration:str):
        """
        ELP:
            -validate input fields
                -validate name
                -validate fee
                -validate duration
            -if course presents
                return error
            -else
                add course
        """
        self.validate_input_fields(name=name,fee=fee,duration=duration)
        
        try:
            self.storage.valid_course(name=name)
        except InvalidCourse:
            self.presenter.raise_exception_for_invalid_course()

        course=self.storage.add_course(name=name,fee=fee,duration=duration)
        return self.presenter.get_add_coure_response(course_id=course)
    
    def validate_input_fields(self,name:str,fee:int,duration:str):

        try:
            self.storage.valid_name_field(name=name)
        except MissingName:
            self.presenter.raise_exception_for_missing_name()
        
        try:
            self.storage.valid_fee_field(fee=fee)
        except MissingFee:
            self.presenter.raise_exception_for_missing_fee()
        
        try:
            self.storage.valid_duration_field(duration=duration)
        except MissingDuration:
            self.presenter.raise_exception_for_missing_duration()