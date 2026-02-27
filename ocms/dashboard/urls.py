from django.urls import path
from .views import AdminAnalyticsView, TopCoursesView

urlpatterns = [
    path('analytics/', AdminAnalyticsView.as_view()),
    path('top-courses/', TopCoursesView.as_view()),
]