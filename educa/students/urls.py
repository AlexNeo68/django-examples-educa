from django.urls import path

from .views import StudentCourseDetailView, StudentCourseListView, StudentEnrollCourseView, StudentRegistrationView


urlpatterns = [
    path('register/', StudentRegistrationView.as_view(), name='student_registration'),
    path('enroll-course/', StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/', StudentCourseListView.as_view(), name='student_course_list'),
    path('courses/<pk>/', StudentCourseDetailView.as_view(), name='student_course_detail'),
    path('courses/<pk>/<module_id>/', StudentCourseDetailView.as_view(), name='student_course_detail_module'),
]
