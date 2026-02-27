from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.cache import cache

from .models import Course
from .serializers import CourseSerializer



class CourseListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        cached_courses = cache.get("course_list")
        if cached_courses:
            return Response(cached_courses)
        
        courses = Course.objects.filter(is_published=True)
        serializer = CourseSerializer(courses, many=True)

        cache.set("course_list", serializer.data, timeout=300)

        return Response(serializer.data)