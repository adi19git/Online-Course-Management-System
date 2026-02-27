from rest_framework import serializers
from .models import Enrollment
from courses.models import Course


class EnrollmentSerializer(serializers.ModelSerializer):

    course_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'course_id', 'status', 'enrolled_at']
        read_only_fields = ['status', 'enrolled_at']

    def create(self, validated_data):
        user = self.context['request'].user
        course_id = validated_data.pop('course_id')

        course = Course.objects.get(id=course_id)

        enrollment, created = Enrollment.objects.get_or_create(
            student=user,
            course=course
        )
        return enrollment