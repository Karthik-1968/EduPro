from abc import abstractmethod
from dataclasses import dataclass
from edu_core.constants.enums import Choices
from typing import Optional

@dataclass
class tokendto:
    access_token:str
    expires_in:int

@dataclass
class Studentdto:
    name:str
    email:str
    age:int

@dataclass
class Teacherdto:
    name:str
    email:str
    age:int

@dataclass
class Coursedto:
    name:str
    fee:int
    duration:str

@dataclass
class CourseTeacherdto:
    teacher_dto:Teacherdto
    course_dto:Coursedto

@dataclass
class CourseStudentdto:
    student_dto:Studentdto
    course_dto:Coursedto

@dataclass
class Assignmentdto:
    name:str
    max_duration_in_mins:int
    assignment_description:str

@dataclass
class CourseAssignmentdto:
    course_dto:Coursedto
    assignment_dto:Assignmentdto

@dataclass
class Submissiondto:
    student_dto:Studentdto
    assignment_dto:Assignmentdto
    submitted_at:str
    grade: Optional[Choices]
    remarks:Optional[str]


class StorageInterface:

    @abstractmethod
    def add_student(self,name:str,email:str,age:int)->int:
        pass

    @abstractmethod
    def valid_student(self,email:str):
        pass

    @abstractmethod
    def valid_name_field(self,name:str):
        pass

    @abstractmethod
    def valid_email_field(self,email:str):
        pass

    @abstractmethod
    def valid_age_field(self,age:int):
        pass

    @abstractmethod
    def check_user(self,email:str):
        pass

    @abstractmethod
    def add_teacher(self,name:str,email:str,age:int)->int:
        pass

    @abstractmethod
    def create_user(self,email:str):
        pass

    @abstractmethod
    def login(self,user_email:str)->tokendto:
        pass

    @abstractmethod
    def valid_teacher(self,email:str)->int:
        pass

    @abstractmethod
    def get_student_details(self,id:int)->Studentdto:
        pass

    @abstractmethod
    def check_student_exists(self,id:int):
        pass

    @abstractmethod
    def get_list_of_students(self,limit:int,offset:int)->list[Studentdto]:
        pass

    @abstractmethod
    def get_teacher_details(self,id:int)->Teacherdto:
        pass

    @abstractmethod
    def check_teacher_exists(self,id:int):
        pass

    @abstractmethod
    def get_list_of_teachers(self,limit:int,offset:int)->list[Teacherdto]:
        pass

    @abstractmethod
    def delete_student(self,id:int):
        pass

    @abstractmethod
    def check_user_authorization(self,student_email:str,user_email:str):
        pass

    @abstractmethod
    def delete_teacher(self,id:int):
        pass

    @abstractmethod
    def valid_fee_field(self,fee:int):
        pass

    @abstractmethod
    def valid_duration_field(self,duration:str):
        pass

    @abstractmethod
    def valid_course(self,name:str):
        pass

    @abstractmethod
    def add_course(self,name:str,fee:int,duration:str)->int:
        pass

    @abstractmethod
    def check_course_exists(self,id:int):
        pass

    @abstractmethod
    def get_course_details(self,id:int)->Coursedto:
        pass

    @abstractmethod
    def get_list_of_courses_details(self,limit:int,offset:int)->list[Coursedto]:
        pass

    @abstractmethod
    def validate_id(self,id:int):
        pass

    @abstractmethod
    def check_if_already_assigned(self,teacher_id:int,course_id:int):
        pass

    @abstractmethod
    def assign_teacher_course(self,teacher_id:int,course_id:int)->CourseTeacherdto:
        pass

    @abstractmethod
    def check_if_already_enrolled(self,student_id:int,course_id:int):
        pass

    @abstractmethod
    def enroll_student_course(self,student_id:int,course_id:int)->CourseStudentdto:
        pass

    @abstractmethod
    def valid_duration_in_mins_field(self,duration:int):
        pass

    @abstractmethod
    def valid_assignment_description_field(self,assignment_description:str):
        pass

    @abstractmethod
    def valid_assignment(self,name:str):
        pass

    @abstractmethod
    def add_assignment(self,name:str,max_duration:int,assign_description:str)->int:
        pass

    @abstractmethod
    def check_assignment_exists(self,id:int):
        pass

    @abstractmethod
    def delete_assignment(self,id:int):
        pass

    @abstractmethod
    def update_assignment(self,name:str,max_duration:int,assign_description:str,id:int)->Assignmentdto:
        pass

    @abstractmethod
    def assignments_of_course(self,limit:int,offset:int,id:int)->list[Assignmentdto]:
        pass

    @abstractmethod
    def check_if_assignment_already_added_to_course(self,course_id:int,assignment_id:int):
        pass

    @abstractmethod
    def add_assignment_to_course(self,course_id:int,assignment_id:int)->CourseAssignmentdto:
        pass

    @abstractmethod
    def validate_submitted_at(self,submitted_at:str):
        pass

    @abstractmethod
    def check_if_already_submitted(self,student_id:int,assignment_id:int):
        pass

    @abstractmethod
    def add_submission(self,student_id:int,assignment_id:int,submitted_at:str)->int:
        pass

    @abstractmethod
    def list_of_submissions(self,limit:int,offset:int,id:int)->list[Submissiondto]:
        pass

    @abstractmethod
    def check_submission_exists(self,id:int):
        pass

    @abstractmethod
    def check_user_is_teacher(self,user_email:str):
        pass

    @abstractmethod
    def check_if_submission_already_graded(self,id=int):
        pass

    @abstractmethod
    def grade_submission(self,id:int)->Choices:
        pass

    @abstractmethod
    def check_if_user_email(self,email:str):
        pass