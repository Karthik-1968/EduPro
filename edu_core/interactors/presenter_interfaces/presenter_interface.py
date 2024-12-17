from abc import abstractmethod
from edu_core.interactors.storage_interfaces.storage_interface import tokendto,Studentdto,Teacherdto,Coursedto,\
CourseTeacherdto,CourseStudentdto,Assignmentdto

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

    @abstractmethod
    def raise_exception_for_invalid_access(self):
        pass

    @abstractmethod
    def get_delete_student_response(self):
        pass

    @abstractmethod
    def get_delete_teacher_response(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_fee(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_duration(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_course(self):
        pass

    @abstractmethod
    def get_add_coure_response(self,course_id:int):
        pass

    @abstractmethod
    def raise_exception_for_invalid_course_id(self):
        pass

    @abstractmethod
    def get_course_details_response(self,course:Coursedto)->list[dict]:
        pass

    @abstractmethod
    def get_list_of_courses_details_response(self,courses:list[Coursedto])->list[dict]:
        pass

    @abstractmethod
    def raise_exception_for_missingid(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_teacherid(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_courseid(self):
        pass

    @abstractmethod
    def get_assign_teacher_course_response(self,teacher_to_course:CourseTeacherdto)->dict:
        pass

    @abstractmethod
    def raise_exception_for_teacher_already_assigned(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_studentid(self):
        pass

    @abstractmethod
    def raise_exception_for_student_already_enrolled(self):
        pass

    @abstractmethod
    def get_enroll_student_course_response(self,course_student_dtos:CourseStudentdto)->dict:
        pass

    @abstractmethod
    def raise_exception_for_missing_duration_in_mins(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_description(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_assignment(self):
        pass

    @abstractmethod
    def get_add_assignment_response(self,assignment_id:int):
        pass

    @abstractmethod
    def raise_exception_for_invalid_assignment_id(self):
        pass

    @abstractmethod
    def get_delete_assignment_response(self):
        pass

    @abstractmethod
    def get_update_assignment_response(self,assignment_dto:Assignmentdto)->dict:
        pass