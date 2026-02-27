from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Review
from .serializers import ReviewSerializer
class AddReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReviewSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Review submitted"})
class CourseReviewsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, course_id):
        reviews = Review.objects.filter(course_id=course_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)