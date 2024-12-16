from abc import abstractmethod
from edu_core.interactors.storage_interfaces.storage_interface import tokendto,Studentdto,Teacherdto

class PresenterInterface:
    
    @abstractmethod
    def get_login_response(self,auth_tokens:tokendto)->dict:
        pass

    @abstractmethod
    def get_add_student_response(self,student_id:int):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_name(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_email(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_age(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_student(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_teacher(self):
        pass

    @abstractmethod
    def get_add_teacher_response(self,teacher_id:int):
        pass

    @abstractmethod
    def get_user_email_response(self):
        pass

    @abstractmethod
    def add_course(self,course_id:int):
        pass

    @abstractmethod
    def add_assignment(self,assignment_id:int):
        pass

    @abstractmethod
    def add_submission(self,submission_id:int):
        pass

    @abstractmethod
    def update_assignment(self,name:str,max_duration:int,assign_description:str):
        pass

    @abstractmethod
    def assign_teacher_course(self,teacher:str,course:str,fee:int,duration:str):
        pass

    @abstractmethod
    def enroll_student_course(self,student:str,course:str,fee:int,duration:int):
        pass

    @abstractmethod
    def add_assignment_course(self,course:str,assignment:str,max_duration:int,assign_description:str):
        pass

    @abstractmethod
    def grade_submission(self,grade:str):
        pass

    @abstractmethod
    def get_student_details_response(self,student:Studentdto)->list[dict]:
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_student_id(self):
        pass

    @abstractmethod
    def get_list_of_students_details_response(self,students:list[Studentdto])->list[dict]:
        pass

    @abstractmethod
    def get_teacher_details_response(self,teacher:Teacherdto)->list[dict]:
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_teacher_id(self):
        pass

    @abstractmethod
    def get_list_of_teachers_details_response(self,teachers:list[Teacherdto])->list[dict]:
        pass