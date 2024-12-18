from edu_core.interactors.presenter_interfaces.presenter_interface import PresenterInterface

from edu_core.interactors.storage_interfaces.storage_interface import Studentdto,Teacherdto,Coursedto,\
CourseTeacherdto,CourseStudentdto,Assignmentdto,CourseAssignmentdto,Submissiondto

from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden, BadRequest
from edu_core.constants.enums import Choices

from edu_core.constants.exception_messages import INVALID_STUDENT,MISSING_NAME,MISSING_EMAIL,MISSING_AGE,INVALID_USER,\
INVALID_TEACHER,INVALID_STUDENT_ID,INVALID_TEACHER_ID,INVALID_ACCESS,MISSING_FEE,MISSING_DURATION, INVALID_COURSE,\
INVALID_COURSE_ID,MISSING_TEACHER_ID,MISSING_COURSE_ID,TEACHER_ALREADY_ASSIGNED,MISSING_STUDENT_ID,\
STUDENT_ALREADY_ENROLLED,MISSING_DURATION_IN_MINS,MISSING_DESCRIPTION,INVALID_ASSIGNMENT,INVALID_ASSIGNMENT_ID,\
MISSING_ASSIGNMENT_ID,ASSIGNMENT_ALREADY_ADDED_TO_COURSE,MISSING_SUBMITTED_AT,ASSIGNMENT_ALREADY_SUBMITTED,\
MISSING_SUBMISSION_ID,INVALID_SUBMISSION_ID,SUBMISSION_ALREADY_GRADED,INVALID_USER_EMAIL


class PresenterImplementation(PresenterInterface):

    def get_login_response(self,auth_details:list)->dict:
        return {
            "access_token":auth_details[0],
            "expires_in":auth_details[1]
        }
    
    def get_add_student_response(self,student_id:int)->dict:
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
    
    def get_add_teacher_response(self,teacher_id:int)->dict:
        return {
            "id":teacher_id
        }
    
    def get_user_email_response(self):
        return {
            "success":"user is created successfully"
        }
    
    def get_student_details_response(self,student_dto:Studentdto)->list[dict]:
        student_details=[]
        student={
            "name": student_dto.name,
           "email": student_dto.email,
            "age" : student_dto.age
        }
        student_details.append(student)

        return student_details
    
    def raise_exception_for_invalid_student_id(self):
        raise NotFound(*INVALID_STUDENT_ID)
    
    def get_list_of_student_details_response(self,student_dtos:list[Studentdto])->list[dict]:
        students_details=[]

        for student_dto in student_dtos:
            student={
                "name":student_dto.name,
                "email":student_dto.email,
                "age":student_dto.age
            }
            students_details.append(student)
        
        return students_details
    
    def get_teacher_details_response(self,teacher_dto:Teacherdto)->list[dict]:
        teacher_details=[]
        teacher={
            "name": teacher_dto.name,
           "email": teacher_dto.email,
            "age" : teacher_dto.age
        }
        teacher_details.append(teacher)

        return teacher_details
    
    def raise_exception_for_invalid_teacher_id(self):
        raise NotFound(*INVALID_TEACHER_ID)
    
    def get_list_of_teacher_details_response(self,teacher_dtos:list[Teacherdto])->list[dict]:
        teachers_details=[]

        for teacher_dto in teacher_dtos:
            teacher={
                "name":teacher_dto.name,
                "email":teacher_dto.email,
                "age":teacher_dto.age
            }
            teachers_details.append(teacher)

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
    
    def raise_exception_for_missing_fee(self):
        raise BadRequest(*MISSING_FEE)
    
    def raise_exception_for_missing_duration(self):
        raise BadRequest(*MISSING_DURATION)
    
    def raise_exception_for_invalid_course(self):
        raise BadRequest(*INVALID_COURSE)
    
    def get_add_coure_response(self,course_id:int)->dict:
        return {
            "id":course_id
        }
    
    def raise_exception_for_invalid_course_id(self):
        raise NotFound(*INVALID_COURSE_ID)
    
    def get_course_details_response(self,course_dto:Coursedto)->list[dict]:
        course_details=[]
        course={
            "name":course_dto.name,
            "fee":course_dto.fee,
            "duration":course_dto.duration
        }
        course_details.append(course)

        return course_details
    
    def get_list_of_courses_details_response(self,course_dtos:list[Coursedto])->list[dict]:
        courses_details=[]

        for course_dto in course_dtos:
            course={
                "name":course_dto.name,
                "fee":course_dto.fee,
                "duration":course_dto.duration
            }
            courses_details.append(course)
        
        return courses_details
    
    def raise_exception_for_missing_teacherid(self):
        raise BadRequest(*MISSING_TEACHER_ID)
    
    def raise_exception_for_missing_courseid(self):
        raise BadRequest(*MISSING_COURSE_ID)
    
    def get_assign_teacher_course_response(self,course_teacher_dtos:CourseTeacherdto)->dict:
        teacher_of_course={
            "teacher":course_teacher_dtos.teacher_dto.name,
            "course":course_teacher_dtos.course_dto.name,
            "fee":course_teacher_dtos.course_dto.fee,
            "duration":course_teacher_dtos.course_dto.duration
        }

        return teacher_of_course
    
    def raise_exception_for_teacher_already_assigned(self):
        raise BadRequest(*TEACHER_ALREADY_ASSIGNED)
    
    def raise_exception_for_missing_studentid(self):
        raise BadRequest(*MISSING_STUDENT_ID)
    
    def raise_exception_for_student_already_enrolled(self):
        raise BadRequest(*STUDENT_ALREADY_ENROLLED)
    
    def get_enroll_student_course_response(self,course_student_dtos:CourseStudentdto)->dict:
        student_in_course={
            "student":course_student_dtos.student_dto.name,
            "course":course_student_dtos.course_dto.name,
            "fee":course_student_dtos.course_dto.fee,
            "duration":course_student_dtos.course_dto.duration
        }
        return student_in_course
    
    def raise_exception_for_missing_duration_in_mins(self):
        raise BadRequest(*MISSING_DURATION_IN_MINS)
    
    def raise_exception_for_missing_description(self):
        raise BadRequest(*MISSING_DESCRIPTION)
    
    def raise_exception_for_invalid_assignment(self):
        raise BadRequest(*INVALID_ASSIGNMENT)
    
    def get_add_assignment_response(self,assignment_id:int)->dict:
        return {
            "id":assignment_id
        }
    
    def raise_exception_for_invalid_assignment_id(self):
        raise NotFound(*INVALID_ASSIGNMENT_ID)
    
    def get_delete_assignment_response(self):
        return {
            "success":"assignment deleted successfully"
        }
    
    def get_update_assignment_response(self,assignment_dto:Assignmentdto)->dict:
        updated_assignment={
            "name":assignment_dto.name,
            "max_duration_in_minutes":assignment_dto.max_duration_in_mins,
            "assignment_description":assignment_dto.assignment_description
        }
        return updated_assignment
    
    def raise_exception_for_missing_assignmentid(self):
        raise BadRequest(*MISSING_ASSIGNMENT_ID)
    
    def get_assignments_of_course_response(self,assignment_dtos:list[Assignmentdto])->list[dict]:
        assignment_details=[]

        for assignment_dto in assignment_dtos:
            assignment={
                "assignment_name":assignment_dto.name
            }
            assignment_details.append(assignment)
        
        return assignment_details
    
    def raise_exception_for_assignment_already_added_to_course(self):
        raise BadRequest(*ASSIGNMENT_ALREADY_ADDED_TO_COURSE)
    
    def get_add_assignment_to_course_response(self,course_assignment_dtos:CourseAssignmentdto)->dict:
        assignment_of_course={
            "course":course_assignment_dtos.course_dto.name,
            "assignment":course_assignment_dtos.assignment_dto.name,
            "max_duration_in_minutes":course_assignment_dtos.assignment_dto.max_duration_in_mins,
            "assignment_description":course_assignment_dtos.assignment_dto.assignment_description
        }
        return assignment_of_course
    
    def raise_exception_for_missing_submittedat(self):
        raise BadRequest(*MISSING_SUBMITTED_AT)
    
    def raise_exception_for_assignment_already_submitted(self):
        raise BadRequest(*ASSIGNMENT_ALREADY_SUBMITTED)
    
    def get_add_submission_response(self,submission_id:int)->dict:
        return {
            "id":submission_id
        }
    
    def get_list_of_submissions_response(self,submission_dtos:list[Submissiondto])->list[dict]:
        submission_details=[]

        for submission_dto in submission_dtos:
            submission={
                "submitted_by":submission_dto.student_dto.name,
                "submitted_at":submission_dto.submitted_at,
                "Grade":submission_dto.grade,
                "remarks":submission_dto.remarks
            }
            submission_details.append(submission)

        return submission_details

    def raise_exception_for_missing_submissionid(self):
        raise BadRequest(*MISSING_SUBMISSION_ID)
    
    def raise_exception_for_invalid_submission_id(self):
        raise NotFound(*INVALID_SUBMISSION_ID)
    
    def raise_exception_for_submission_already_graded(self):
        raise BadRequest(*SUBMISSION_ALREADY_GRADED)
    
    def get_grade_submission_response(self,grade:Choices)->dict:
        return {
            "grade":grade
        }
    
    def get_logout_response(self):
        return {
            "success":"successfully logged out"
        }
    
    def raise_exception_for_invalid_user_email(self):
        raise BadRequest(*INVALID_USER_EMAIL)