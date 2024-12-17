from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from edu_core.interactors.storage_interfaces.storage_interface import tokendto,Studentdto,Teacherdto,Coursedto,\
CourseTeacherdto,CourseStudentdto,Assignmentdto
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden, BadRequest
from edu_core.constants.exception_messages import INVALID_STUDENT,MISSING_NAME,MISSING_EMAIL,MISSING_AGE,INVALID_USER,\
INVALID_TEACHER,INVALID_STUDENT_ID,INVALID_TEACHER_ID,INVALID_ACCESS,MISSING_FEE,MISSING_DURATION, INVALID_COURSE,\
INVALID_COURSE_ID,MISSING_TEACHER_ID,MISSING_COURSE_ID,TEACHER_ALREADY_ASSIGNED,MISSING_STUDENT_ID,\
STUDENT_ALREADY_ENROLLED,MISSING_DURATION_IN_MINS,MISSING_DESCRIPTION,INVALID_ASSIGNMENT,INVALID_ASSIGNMENT_ID


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
        raise BadRequest(*MISSING_NAME)
    
    def raise_exception_for_missing_email(self):
        raise BadRequest(*MISSING_EMAIL)
    
    def raise_exception_for_missing_age(self):
        raise BadRequest(*MISSING_AGE)
    
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
    
    def raise_exception_for_invalid_access(self):
        raise Forbidden(*INVALID_ACCESS)
    
    def get_delete_student_response(self):
        return {
            "success":"student is deleted successfully"
        }
    
    def get_delete_teacher_response(self):
        return {
            "success":"teacher is deleted successfully"
        }
    
    def raise_exception_for_missing_age(self):
        raise BadRequest(*MISSING_FEE)
    
    def raise_exception_for_missing_duration(self):
        raise BadRequest(*MISSING_DURATION)
    
    def raise_exception_for_invalid_course(self):
        raise BadRequest(*INVALID_COURSE)
    
    def get_add_coure_response(self,course_id:int):
        return {
            "id":course_id
        }
    
    def raise_exception_for_invalid_course_id(self):
        raise NotFound(*INVALID_COURSE_ID)
    
    def get_course_details_response(self,course:Coursedto)->list[dict]:
        course_details=[]
        d={
            "name":course.name,
            "fee":course.fee,
            "duration":course.duration
        }
        course_details.append(d)
        return course_details
    
    def get_list_of_courses_details_response(self,courses:list[Coursedto])->list[dict]:
        courses_details=[]
        for course in courses:
            d={
                "name":course.name,
                "fee":course.fee,
                "duration":course.duration
            }
            courses_details.append(d)
        return courses_details
    
    def raise_exception_for_missing_teacherid(self):
        raise BadRequest(*MISSING_TEACHER_ID)
    
    def raise_exception_for_missing_courseid(self):
        raise BadRequest(*MISSING_COURSE_ID)
    
    def get_assign_teacher_course_response(self,course_teacher_dtos:CourseTeacherdto)->dict:
        d={
            "teacher":course_teacher_dtos.teacher_dto.name,
            "course":course_teacher_dtos.course_dto.name,
            "fee":course_teacher_dtos.course_dto.fee,
            "duration":course_teacher_dtos.course_dto.duration
        }
        return d
    
    def raise_exception_for_teacher_already_assigned(self):
        raise BadRequest(*TEACHER_ALREADY_ASSIGNED)
    
    def raise_exception_for_missing_studentid(self):
        raise BadRequest(*MISSING_STUDENT_ID)
    
    def raise_exception_for_student_already_enrolled(self):
        raise BadRequest(*STUDENT_ALREADY_ENROLLED)
    
    def get_enroll_student_course_response(self,course_student_dtos:CourseStudentdto)->dict:
        d={
            "student":course_student_dtos.student_dto.name,
            "course":course_student_dtos.course_dto.name,
            "fee":course_student_dtos.course_dto.fee,
            "duration":course_student_dtos.course_dto.duration
        }
        return d
    
    def raise_exception_for_missing_duration_in_mins(self):
        raise BadRequest(*MISSING_DURATION_IN_MINS)
    
    def raise_exception_for_missing_description(self):
        raise BadRequest(*MISSING_DESCRIPTION)
    
    def raise_exception_for_invalid_assignment(self):
        raise BadRequest(*INVALID_ASSIGNMENT)
    
    def get_add_assignment_response(self,assignment_id:int):
        return {
            'id':assignment_id
        }
    
    def raise_exception_for_invalid_assignment_id(self):
        raise NotFound(*INVALID_ASSIGNMENT_ID)
    
    def get_delete_assignment_response(self):
        return {
            "Success":"Assignment deleted successfully"
        }
    
    def get_update_assignment_response(self,assignment_dto:Assignmentdto)->dict:
        d={
            "name":assignment_dto.name,
            "max_duration_in_minutes":assignment_dto.max_duration_in_mins,
            "assignment_description":assignment_dto.assignment_description
        }
        return d