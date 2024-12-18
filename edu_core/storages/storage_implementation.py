from edu_core.models import Student,Teacher,Course,User,Assignment,Submission
from edu_core.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_users.interfaces.service_interface import ServiceInterface

from edu_core.exceptions.custom_exceptions import InvalidStudent, MissingName, MissingEmail, MissingAge, InvalidUser,\
InvalidTeacher, InvalidStudentId, InvalidTeacherId, InvalidAccess, MissingFee, MissingDuration, InvalidCourse,\
InvalidCourseId,MissingId,TeacherAlreadyAssigned,StudentAlreadyEnrolled,MissingDurationInMins,MissingDescription,\
InvalidAssignment,InvalidAssignmentId,AssignmentAlreadyAddedtoCourse,MissingSubmittedAt,AssignmentAlreadySubmitted,\
InvalidSubmissionId,SubmissionAlreadyGraded

from edu_core.interactors.storage_interfaces.storage_interface import tokendto, Studentdto, Teacherdto, Coursedto,\
 CourseTeacherdto, CourseStudentdto, Assignmentdto, CourseAssignmentdto,Submissiondto
from edu_core.constants.enums import Choices

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
    
    def check_user_authorization(self,email:str,user_email:str):
        if email!=user_email:
            raise InvalidAccess
    
    def delete_student(self,id:int):
        Student.objects.get(id=id).delete()
    
    def delete_teacher(self,id:int):
        Teacher.objects.get(id=id).delete()

    def valid_fee_field(self,fee:int):
        fee_not_present=not fee
        if fee_not_present:
            raise MissingFee
    
    def valid_duration_field(self,duration:str):
        duration_not_present=not duration
        if duration_not_present:
            raise MissingDuration
        
    def valid_course(self,name:str):
        if Course.objects.filter(name=name).exists():
            raise InvalidCourse
    
    def add_course(self,name:str,fee:int,duration:str)->int:
        course=Course.objects.create(name=name,fee=fee,duration=duration)
        course_id=course.id
        return course_id
    
    def check_course_exists(self,id:int):
        if Course.objects.filter(id=id).exists()==False:
            raise InvalidCourseId
        
    def get_course_details(self,id:int)->Coursedto:
        course=Course.objects.get(id=id)
        return course
    
    def get_list_of_courses_details(self,limit:int,offset:int)->list[Coursedto]:
        courses=Course.objects.all()[offset:offset+limit]
        courses=[course for course in courses]
        return courses
    
    def validate_id(self,id:int):
        id_not_present=not id
        if id_not_present:
            raise MissingId
    
    def check_if_already_assigned(self,teacher_id:int,course_id:int):
        teacher=Teacher.objects.get(id=teacher_id)
        if Course.objects.filter(id=course_id,teacher=teacher).exists():
            raise TeacherAlreadyAssigned
        
    def assign_teacher_course(self,teacher_id:int,course_id:int)->CourseTeacherdto:
        teacher=Teacher.objects.get(id=teacher_id)
        course=Course.objects.get(id=course_id)
        course.teacher.add(teacher)
        course_dto=self.convert_course_obj_to_dto(course)
        teacher_dto=self.convert_teacher_obj_to_dto(teacher)
        return CourseTeacherdto(
            teacher_dto=teacher_dto,
            course_dto=course_dto
        )

    @staticmethod
    def convert_course_obj_to_dto(course):
        course_dto=Coursedto(name=course.name,
                             fee=course.fee,
                             duration=course.duration)
        return course_dto
    
    @staticmethod
    def convert_teacher_obj_to_dto(teacher):
        teacher_dto=Teacherdto(name=teacher.name,
                               email=teacher.email,
                               age=teacher.age)
        return teacher_dto
    
    def check_if_already_enrolled(self,student_id:int,course_id:int):
        student=Student.objects.get(id=student_id)
        if Course.objects.filter(id=course_id,student=student).exists():
            raise StudentAlreadyEnrolled
        
    def enroll_student_course(self,student_id:int,course_id:int)->CourseStudentdto:
        student=Student.objects.get(id=student_id)
        course=Course.objects.get(id=course_id)
        course.student.add(student)
        course_dto=self.convert_course_obj_to_dto(course)
        student_dto=self.convert_student_obj_to_dto(student)
        return CourseStudentdto(
            student_dto=student_dto,
            course_dto=course_dto
        )
    
    @staticmethod
    def convert_student_obj_to_dto(student):
        return Studentdto(
            name=student.name,
            email=student.email,
            age=student.age
        )

    def valid_duration_in_mins_field(self,duration:int):
        duration_not_given=not duration
        if duration_not_given:
            raise MissingDurationInMins
    
    def valid_assignment_description_field(self,assignment_description:str):
        assigment_description_not_given=not assignment_description
        if assigment_description_not_given:
            raise MissingDescription
        
    def valid_assignment(self,name:str):
        if Assignment.objects.filter(name=name).exists():
            raise InvalidAssignment
        
    def add_assignment(self,name:str,max_duration:int,assign_description:str)->int:
        assignment=Assignment.objects.create(name=name,max_duration=max_duration,assign_description=assign_description)
        assignment_id=assignment.id
        return assignment_id
    
    def check_assignment_exists(self,id:int):
        if Assignment.objects.filter(id=id).exists()==False:
            raise InvalidAssignmentId
        
    def delete_assignment(self,id:int):
        Assignment.objects.get(id=id).delete()

    def update_assignment(self,name:str,max_duration:int,assign_description:str,id:int)->Assignmentdto:
        assignment=Assignment.objects.get(id=id)
        assignment.name=name
        assignment.max_duration=max_duration
        assignment.assign_description=assign_description
        assignment.save()
        assignment_dto=self.convert_assignment_obj_to_dto(assignment)
        return assignment_dto
    
    @staticmethod
    def convert_assignment_obj_to_dto(assignment):
        return Assignmentdto(
            name=assignment.name,
            max_duration_in_mins=assignment.max_duration,
            assignment_description=assignment.assign_description
        )
    
    def assignments_of_course(self,limit:int,offset:int,id:int)->list[Assignmentdto]:
        course=Course.objects.get(id=id)
        assignments=Assignment.objects.filter(course=course)
        assignment_dtos=[]
        for assignment in assignments:
            assignment_dto=self.convert_assignment_obj_to_dto(assignment)
            assignment_dtos.append(assignment_dto)
        assignment_dtos=assignment_dtos[offset:offset+limit]
        return assignment_dtos
    
    def check_if_assignment_already_added_to_course(self,course_id:int,assignment_id:int):
        assignment=Assignment.objects.get(id=assignment_id)
        if assignment.course:
            if assignment.course.id==course_id:
                raise AssignmentAlreadyAddedtoCourse
        
    def add_assignment_to_course(self,course_id:int,assignment_id:int)->CourseAssignmentdto:
        course=Course.objects.get(id=course_id)
        assignment=Assignment.objects.get(id=assignment_id)
        assignment.course=course
        assignment.save()
        course_dto=self.convert_course_obj_to_dto(course)
        assignment_dto=self.convert_assignment_obj_to_dto(assignment)
        return CourseAssignmentdto(
            course_dto =  course_dto,
            assignment_dto = assignment_dto
        )
    
    def validate_submitted_at(self,submitted_at:str):
        submitted_at_not_present=not submitted_at
        if submitted_at_not_present:
            raise MissingSubmittedAt
        
    def check_if_already_submitted(self,student_id:int,assignment_id:int):
        if Submission.objects.filter(student_id=student_id,assignment_id=assignment_id).exists():
            raise AssignmentAlreadySubmitted
        
    def add_submission(self,student_id:int,assignment_id:int,submitted_at:str)->int:
        student=Student.objects.get(id=student_id)
        assignment=Assignment.objects.get(id=assignment_id)
        submission=Submission.objects.create(student=student,assignment=assignment,submitted_at=submitted_at)
        submission_id=submission.id
        return submission_id
    
    def list_of_submissions(self,limit:int,offset:int,id:int)->list[Submissiondto]:
        submissions=Submission.objects.filter(assignment_id=id)
        submission_dtos=[]
        for submission in submissions:
            submission_dto=self.convert_submission_obj_to_dto(submission)
            submission_dtos.append(submission_dto)
        submission_dtos=submission_dtos[offset:offset+limit]
        return submission_dtos

    @staticmethod
    def convert_submission_obj_to_dto(submission):
        return Submissiondto(
            student_dto=Studentdto(name=submission.student.name,email=submission.student.email,age=submission.student.age),
            assignment_dto=Assignmentdto(name=submission.assignment.name,max_duration_in_mins=submission.assignment.max_duration,\
                                         assignment_description=submission.assignment.assign_description),
            submitted_at=submission.submitted_at,
            grade=submission.Grade,
            remarks=submission.remarks
        )
    
    def check_submission_exists(self,id:int):
        if Submission.objects.filter(id=id).exists()==False:
            raise InvalidSubmissionId
        
    def check_user_is_teacher(self,user_email:str):
        teachers=Teacher.objects.all()
        teacher_emails=[teacher.email for teacher in teachers]
        if user_email not in teacher_emails:
            raise InvalidAccess
    
    def check_if_submission_already_graded(self,id=int):
        submission=Submission.objects.get(id=id)
        if submission.Grade:
            raise SubmissionAlreadyGraded
    
    def grade_submission(self,id:int)->Choices:
        submission=Submission.objects.get(id=id)
        submission.Grade="B"
        submission.remarks="Good"
        submission.save
        return submission.Grade