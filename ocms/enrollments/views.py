from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Enrollment
from .serializers import EnrollmentSerializer
from courses.serializers import CourseSerializer
class EnrollCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EnrollmentSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Successfully enrolled"})

class MyCoursesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        enrollments = Enrollment.objects.filter(student=request.user)
        courses = [en.course for en in enrollments]
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)