from django.urls import path
from . import views

# app_name = 'home'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('teachers/', views.TeacherListView.as_view(), name='teacher-list'),
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('students/<int:teacher_id>/', views.students_for_teacher, name='students-for-teacher'),
    path('teachers/<int:student_id>/', views.teachers_for_student, name='teachers-for-student'),
    path('select-pair/', views.select_pair, name='select_pair'),
    path('certificate-created/', views.certificate_created, name='certificate_created'),
]
