from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.exceptions.custom_exceptions import MissingName,MissingDurationInMins,MissingDescription,MissingId,\
InvalidAssignmentId

class UpdateAssignmentInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage=storage
        self.presenter=presenter

    def update_assignment(self,name:str,max_duration_in_mins:int,assignment_description:str,current_assignment:int):
        """
        "ELP":
            -validate input details
                -validate name
                -validate max_duration_in_mins
                -valiate assignment_description
                -validate current_assignment
            -check if current assignment exists
            -update assignment
        """
        check_input_exists=self.validate_input_data(name=name,max_duration_in_mins=max_duration_in_mins,assignment_description=assignment_description,current_assignment=current_assignment)
        if check_input_exists:
            return check_input_exists
        
        try:
            self.storage.check_assignment_exists(id=current_assignment)
        except InvalidAssignmentId:
            return self.presenter.raise_exception_for_invalid_assignment_id()
        
        assignment_dto=self.storage.update_assignment(name=name,max_duration=max_duration_in_mins,assign_description=assignment_description,id=current_assignment)
        return self.presenter.get_update_assignment_response(assignment_dto=assignment_dto)
    
    def validate_input_data(self,name:str,max_duration_in_mins:int,assignment_description:str,current_assignment:int):

        try:
            self.storage.valid_name_field(name=name)
        except MissingName:
            return self.presenter.raise_exception_for_missing_name()
        
        try:
            self.storage.validate_id(id=current_assignment)
        except MissingId:
            return self.presenter.raise_exception_for_missing_assignmentid()
        

        try:
            self.storage.valid_duration_in_mins_field(duration=max_duration_in_mins)
        except MissingDurationInMins:
            return self.presenter.raise_exception_for_missing_duration_in_mins()
        
        try:
            self.storage.valid_assignment_description_field(assignment_description=assignment_description)
        except MissingDescription:
            return self.presenter.raise_exception_for_missing_description()
        
        return None