from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import InvalidAssignment,MissingName,MissingDurationInMins,MissingDescription

class AddAssignmentInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage=storage
        self.presenter=presenter

    def add_assignment(self,name:str,max_duration_in_minutes:int,assignment_description:str):
        """
        ELP:
        - Validate input
            - validate name
            - validate max_duration_in_mins
            - validate assignment_description
        - check if assignment exists
            - if yes:
                return error
            - else:
                create a assignment

        """
        self.validate_input_data(name=name,max_duration_in_mins=max_duration_in_minutes,\
                                 assignment_description=assignment_description)

        try:
            self.storage.valid_assignment(name=name)
        except InvalidAssignment:
            self.presenter.raise_exception_for_invalid_assignment()
        
        assignment=self.storage.add_assignment(name=name,max_duration=max_duration_in_minutes,assign_description=assignment_description)
        return self.presenter.get_add_assignment_response(assignment_id=assignment)
    
    def validate_input_data(self,name:str,max_duration_in_mins:int,assignment_description:str):
        try:
            self.storage.valid_name_field(name=name)
        except MissingName:
            self.presenter.raise_exception_for_missing_name()

        try:
            self.storage.valid_duration_in_mins_field(duration=max_duration_in_mins)
        except MissingDurationInMins:
            self.presenter.raise_exception_for_missing_duration_in_mins()
        
        try:
            self.storage.valid_assignment_description_field(assignment_description=assignment_description)
        except MissingDescription:
            self.presenter.raise_exception_for_missing_description()
