from django.conf.urls import url
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    url(r'^register/$', views.StudentRegistrationView.as_view(), name='student_registration'),
    url(r'^enroll-course/$', views.StudentEnrollCourseView.as_view(),
        name='student_enroll_course'),
    url(r'^courses/$', views.StudentCourseListView.as_view(),
        name='student_course_list'),
    url(r'^courses/(?P<pk>\d+)/$', 
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail'),
    url(r'^courses/(?P<pk>\d+)/(?P<module_id>\d+)/', 
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail_module'),
]