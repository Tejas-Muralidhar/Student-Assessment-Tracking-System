from django.urls import path
from .views import ADMFacViewMapping,AdmFacMapSub,ADMUserAddEdit, AdmViewFaculty,AdmViewStudentAttendance,AdmViewStudentMarks,AdmViewStudents,AdmDeleteSubject,AdmViewSubjects,AdmDeleteUser,AdmViewUsers,AdmAddEditSubject

urlpatterns = [
    path('map-faculty-subject/',AdmFacMapSub,name='AdmFacMapSub'),
    path('view-faculty/',AdmViewFaculty,name='AdmViewFaculty'),
    path('view-student-attendance/',AdmViewStudentAttendance,name='AdmViewStudentAttendance'),
    path('view-student-marks/',AdmViewStudentMarks,name='AdmViewStudentMarks'),
    path('view-students/',AdmViewStudents,name="AdmViewStudents"),
    path('delete-subject/',AdmDeleteSubject,name="AdmDeleteSubject"),
    path('view-subjects/',AdmViewSubjects,name="AdmViewSubjects"),
    path('delete-user/',AdmDeleteUser,name="AdmDeleteUser"),
    path('view-users/',AdmViewUsers,name="AdmViewUsers"),
    path("add-edit-subject/",AdmAddEditSubject,name="AdmAddEditSubject"),
    path("view-faculty-mapping/",ADMFacViewMapping,name="ADMFacViewMapping"),
    path("add-edit-user/",ADMUserAddEdit,name="ADMUserAddEdit"),
]