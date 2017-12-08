from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.StudentRegistrationView.as_view(), name='student_registration'),
    url(r'^enroll-course/$', views.StudentEnrollCourseView.as_view(),
        name='student_enroll_course'),
    url(r'^courses/$', views.StudentCourseListView.as_view(),
        name='student_course_list'),
    url(r'^courses/(?P<pk>\d+)/$', views.StudentCourseDetailView.as_view(),
        name='student_course_detail'),
    url(r'^courses/(?P<pk>\d+)/(?P<module_id>\d+)/', views.StudentCourseDetailView.as_view(),
        name='student_course_detail_module'),
]