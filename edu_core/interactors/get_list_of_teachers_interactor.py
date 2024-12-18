from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from edu_core.exceptions.custom_exceptions import InvalidTeacherId


class ListofTeachersInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def list_of_teachers(self,limit:int,offset:int,search:int,presenter:PresenterInterface):
        """
        ELP:
        if search
            if teacher exists
                return teacher details
            else
                return error
        else
            return teacher details based on given limit and offset
        """
        if search:

            try:
                self.storage.check_teacher_exists(id=search)
            except InvalidTeacherId:
                return presenter.raise_exception_for_invalid_teacher_id()
            
            teacher_dto=self.storage.get_teacher_details(id=search)
            return presenter.get_teacher_details_response(teacher_dto=teacher_dto)
        else:
            teacher_dtos=self.storage.get_list_of_teachers(limit=limit,offset=offset)
            return presenter.get_list_of_teacher_details_response(teacher_dtos=teacher_dtos)