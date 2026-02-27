from django.urls import path
from .views import AddReviewView, CourseReviewsView

urlpatterns = [
    path('add-review/', AddReviewView.as_view()),
    path('course/<int:course_id>/', CourseReviewsView.as_view()),
]