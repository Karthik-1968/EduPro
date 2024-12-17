from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.exceptions.custom_exceptions import InvalidAssignmentId,MissingId

class DeleteAssignment:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def delete_assignment(self,assignment_id:int,presenter:PresenterInterface):

        """
        ELP:
            -validate input
                -validate id
            -check if assignment present
            -delete assignment
        """
        try:
            self.storage.validate_id(id=assignment_id)
        except MissingId:
            return presenter.raise_exception_for_missingid()
        
        try:
            self.storage.check_assignment_exists(id=assignment_id)
        except InvalidAssignmentId:
            return presenter.raise_exception_for_invalid_assignment_id()
        
        self.storage.delete_assignment(id=assignment_id)
        return presenter.get_delete_assignment_response()
