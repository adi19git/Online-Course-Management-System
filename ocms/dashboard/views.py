from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.core.cache import cache

from accounts.models import User
from courses.models import Course
from enrollments.models import Enrollment
from django.db.models import Count
class AdminAnalyticsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_users = User.objects.count()
        total_courses = Course.objects.count()
        total_enrollments = Enrollment.objects.count()

        return Response({
            "total_users": total_users,
            "total_courses": total_courses,
            "total_enrollments": total_enrollments
        })


class TopCoursesView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        cached_data = cache.get("top_courses")
        if cached_data:
            return Response(cached_data)
        top_courses = (
            Course.objects
            .annotate(enroll_count=Count('enrollment'))
            .order_by('-enroll_count')[:5]
            .values('id', 'title', 'enroll_count')
        )
        result = list(top_courses)

        cache.set("top_courses", result, timeout=300)

        return Response(result)