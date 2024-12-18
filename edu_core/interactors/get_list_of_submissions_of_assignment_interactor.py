from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.exceptions.custom_exceptions import MissingId,InvalidAssignmentId


class ListofSubmissionsInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage=storage
        self.presenter=presenter

    def list_of_submissions(self,limit:int,offset:int,id:int):
        """
        ELP:
            -validating input details
                -validate id
            -check if assignment exists
            -list all submissions of an assignment
        """
        try:
            self.storage.validate_id(id=id)
        except MissingId:
            return self.presenter.raise_exception_for_missing_assignmentid()
        
        try:
            self.storage.check_assignment_exists(id=id)
        except InvalidAssignmentId:
            return self.presenter.raise_exception_for_invalid_assignment_id()

        submission_dtos=self.storage.list_of_submissions(limit=limit,offset=offset,id=id)
        return self.presenter.get_list_of_submissions_response(submission_dtos=submission_dtos)