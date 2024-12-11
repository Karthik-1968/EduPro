from django.conf.urls import include
from django.urls import re_path

from edu_core.build.view_environments.user_email_.router import user_email_
from edu_core.build.view_environments.login_.router import login_
from edu_core.build.view_environments.logout_.router import logout_
from edu_core.build.view_environments.all_students_.router import all_students_
from edu_core.build.view_environments.all_teachers_.router import all_teachers_
from edu_core.build.view_environments.add_student_.router import add_student_
from edu_core.build.view_environments.add_teacher_.router import add_teacher_
from edu_core.build.view_environments.delete_student_.router import delete_student_
from edu_core.build.view_environments.delete_teacher_.router import delete_teacher_
from edu_core.build.view_environments.all_courses.router import all_courses
from edu_core.build.view_environments.add_course.router import add_course
from edu_core.build.view_environments.assign_teacher_course.router import assign_teacher_course
from edu_core.build.view_environments.enroll_student_course.router import enroll_student_course
from edu_core.build.view_environments.all_assignments_course.router import all_assignments_course
from edu_core.build.view_environments.add_assignment_course.router import add_assignment_course
from edu_core.build.view_environments.add_assignment.router import add_assignment
from edu_core.build.view_environments.update_assignment_.router import update_assignment_
from edu_core.build.view_environments.delete_assignment.router import delete_assignment
from edu_core.build.view_environments.all_submissions_assignment.router import all_submissions_assignment
from edu_core.build.view_environments.add_submission.router import add_submission
from edu_core.build.view_environments.grade_submission.router import grade_submission


base_path = "api/edu_core"

api_paths = [
    re_path(r'^user/email/$', user_email_),
    re_path(r'^login/$', login_),
    re_path(r'^logout/$', logout_),
    re_path(r'^all/students/$', all_students_),
    re_path(r'^all/teachers/$', all_teachers_),
    re_path(r'^add/student/$', add_student_),
    re_path(r'^add/teacher/$', add_teacher_),
    re_path(r'^delete/student/$', delete_student_),
    re_path(r'^delete/teacher/$', delete_teacher_),
    re_path(r'^all/courses/$', all_courses),
    re_path(r'^add/course/$', add_course),
    re_path(r'^assign/teacher/course/$', assign_teacher_course),
    re_path(r'^enroll/student/course/$', enroll_student_course),
    re_path(r'^all/assignments/course/$', all_assignments_course),
    re_path(r'^add/assignment/course/$', add_assignment_course),
    re_path(r'^add/assignment/$', add_assignment),
    re_path(r'^update/assignment/$', update_assignment_),
    re_path(r'^delete/assignment/$', delete_assignment),
    re_path(r'^all/submissions/assignment/$', all_submissions_assignment),
    re_path(r'^add/submission/$', add_submission),
    re_path(r'^grade/submission/$', grade_submission),
]


urlpatterns = [
    re_path(r'^{base_path}'.format(base_path=base_path), include(api_paths))
]
