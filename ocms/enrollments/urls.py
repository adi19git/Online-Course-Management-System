from django.urls import path
from .views import EnrollCourseView, MyCoursesView

urlpatterns = [
    path('enroll/', EnrollCourseView.as_view()),
    path('my-courses/', MyCoursesView.as_view()),
]