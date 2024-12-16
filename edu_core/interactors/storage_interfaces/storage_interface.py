from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class tokendto:
    access_token:str
    expires_in:int

class Studentdto:
    name:str
    email:str
    age:int

class Teacherdto:
    name:str
    email:str
    age:int

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