from edu_core.models import Student,Teacher,Course,User,Assignment,Submission
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_users.interfaces.service_interface import ServiceInterface
from edu_core.exceptions.custom_exceptions import InvalidStudent, MissingName, MissingEmail, MissingAge, InvalidUser,\
InvalidTeacher, InvalidStudentId, InvalidTeacherId
from edu_core.interactors.storage_interfaces.storage_interface import tokendto, Studentdto, Teacherdto


class StorageImplementation(StorageInterface):

    def add_student(self,name:str,email:str,age:int)->int:
        student=Student.objects.create(name=name,email=email,age=age)
        student_id=student.id
        return student_id
    
    def add_teacher(self,name:str,email:str,age:int)->int:
        teacher=Teacher.objects.create(name=name,email=email,age=age)
        teacher_id=teacher.id
        return teacher_id
    
    def create_user(self,email:str):
        User.objects.create(email=email)

    def check_user(self,email:str):
        if User.objects.filter(email=email).exists():
            raise InvalidUser

    def valid_name_field(self,name:str):
        name_not_present=not name
        if name_not_present:
            raise MissingName
        
    def valid_email_field(self,email:str):
        email_not_present=not email
        if email_not_present:
            raise MissingEmail
        
    def valid_age_field(self,age:int):
        age_not_present=not age
        if age_not_present:
            raise MissingAge

    def valid_student(self,email:str):
        if Student.objects.filter(email=email).exists():
            raise InvalidStudent
        
    def login(self,user_email:str)->tokendto:
        user=User.objects.get(email=user_email).user_id
        service_interface = ServiceInterface()
        auth_tokens = service_interface.create_auth_tokens_for_user(user)
        return auth_tokens
    
    def valid_teacher(self,email:str)->int:
        if Teacher.objects.filter(email=email).exists():
            raise InvalidTeacher
    
    def check_student_exists(self,id:int):
        if Student.objects.filter(id=id).exists()==False:
            raise InvalidStudentId
    
    def get_student_details(self,id:int)->Studentdto:
        student=Student.objects.get(id=id)
        return student
    
    def get_list_of_students(self,limit:int,offset:int)->list[Studentdto]:
        students=Student.objects.all()[offset:offset+limit]
        students=[student for student in students]
        return students
    
    def check_teacher_exists(self,id:int):
        if Teacher.objects.filter(id=id).exists()==False:
            raise InvalidTeacherId
    
    def get_teacher_details(self,id:int)->Teacherdto:
        teacher=Teacher.objects.get(id=id)
        return teacher
    
    def get_list_of_teachers(self,limit:int,offset:int)->list[Teacherdto]:
        teachers=Teacher.objects.all()[offset:offset+limit]
        teachers=[teacher for teacher in teachers]
        return teachers