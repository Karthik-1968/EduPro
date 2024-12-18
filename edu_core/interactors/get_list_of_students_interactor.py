from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import InvalidStudentId


class ListofStudentsInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def list_of_students(self,limit:int,offset:int,search:int,presenter:PresenterInterface):
        """
        ELP:
            -if search
                -check if student exists
                -get student details
            -get list of student details
        """

        if search:
            try:
                self.storage.check_student_exists(id=search)
            except InvalidStudentId:
                presenter.raise_exception_for_invalid_student_id()
            
            student_dto=self.storage.get_student_details(id=search)
            return presenter.get_student_details_response(student_dto=student_dto)
        else:
            student_dtos=self.storage.get_list_of_students(limit=limit,offset=offset)
            return presenter.get_list_of_student_details_response(student_dtos=student_dtos)
    
            
