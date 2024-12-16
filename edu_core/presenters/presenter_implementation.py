from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import tokendto,Studentdto,Teacherdto
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden, Unauthorized, BadRequest
from edu_core.constants.exception_messages import INVALID_STUDENT,MISSING_NAME,MISSING_EMAIL,MISSING_AGE,INVALID_USER,INVALID_TEACHER,\
INVALID_STUDENT_ID,INVALID_TEACHER_ID


class PresenterImplementation(PresenterInterface):

    def get_login_response(self,auth_tokens:tokendto):
        return {
            "access_token":auth_tokens.access_token,
            "expires_in":auth_tokens.expires_in
        }
    
    def get_add_student_response(self,student_id:int):
        return {
            "id": student_id
        }
    
    def raise_exception_for_invalid_student(self):
        raise BadRequest(*INVALID_STUDENT)
    
    def raise_exception_for_invalid_teacher(self):
        raise BadRequest(*INVALID_TEACHER)
    
    def raise_exception_for_missing_name(self):
        raise NotFound(*MISSING_NAME)
    
    def raise_exception_for_missing_email(self):
        raise NotFound(*MISSING_EMAIL)
    
    def raise_exception_for_missing_age(self):
        raise NotFound(*MISSING_AGE)
    
    def raise_exception_for_invalid_user(self):
        raise BadRequest(*INVALID_USER)
    
    def get_add_teacher_response(self,teacher_id:int):
        return {
            "id":teacher_id
        }
    
    def get_user_email_response(self):
        return {
            "success":"user is successfully created"
        }
    
    def add_course(self,course_id:int):
        return {
            "id":course_id
        }
    
    def add_assignment(self,assignment_id:int):
        return {
            "id":assignment_id
        }
    
    def add_submission(self,submission_id:int):
        return {
            "id":submission_id
        }
    
    def update_assignment(self,name:str,max_duration:int,assign_description:str):
        return {
            "name":name,
            "max_duration_in_minutes":max_duration,
            "assignment_description":assign_description
        }
    
    def assign_teacher_course(self,teacher:str,course:str,fee:int,duration:str):
        return {
            "teacher":teacher,
            "course":course,
            "fee":fee,
            "duration":duration
        }
    
    def enroll_student_course(self,student:str,course:str,fee:int,duration:int):
        return {
            "student":student,
            "course":course,
            "fee":fee,
            "duration":duration
        }
    
    def add_assignment_course(self,course:str,assignment:str,max_duration:int,assign_description:str):
        return {
            "course":course,
            "assignment":assignment,
            "max_duration_in_minutes":max_duration,
            "assignment_description":assign_description
        }
    
    def grade_submission(self,grade:str):
        return {
            "grade":grade
        }
    
    def get_student_details_response(self,student:Studentdto)->list[dict]:
        student_details=[]
        d={
            "name": student.name,
           "email": student.email,
            "age" : student.age
        }
        student_details.append(d)
        return student_details
    
    def raise_exception_for_invalid_student_id(self):
        raise NotFound(*INVALID_STUDENT_ID)
    
    def get_list_of_student_details_response(self,students:list[Studentdto])->list[dict]:
        students_details=[]
        for student in students:
            d={
                "name":student.name,
                "email":student.email,
                "age":student.age
            }
            students_details.append(d)
        return students_details
    
    def get_teacher_details_response(self,teacher:Teacherdto)->list[dict]:
        teacher_details=[]
        d={
            "name": teacher.name,
           "email": teacher.email,
            "age" : teacher.age
        }
        teacher_details.append(d)
        return teacher_details
    
    def raise_exception_for_invalid_teacher_id(self):
        raise NotFound(*INVALID_TEACHER_ID)
    
    def get_list_of_teacher_details_response(self,teachers:list[Teacherdto])->list[dict]:
        teachers_details=[]
        for teacher in teachers:
            d={
                "name":teacher.name,
                "email":teacher.email,
                "age":teacher.age
            }
            teachers_details.append(d)
        return teachers_details