from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import InvalidStudentId

class ListofStudents:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def list_of_students(self,limit:int,offset:int,search:int,presenter:PresenterInterface):
        if search:
            try:
                self.storage.check_student_exists(id=search)
            except InvalidStudentId:
                return presenter.raise_exception_for_invalid_student_id()
            
            student=self.storage.get_student_details(id=search)
            return presenter.get_student_details_response(student)
        else:
            students=self.storage.get_list_of_students(limit=limit,offset=offset)
            return presenter.get_list_of_student_details_response(students)
    
            
