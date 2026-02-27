from rest_framework import serializers
from .models import Review
from courses.models import Course


class ReviewSerializer(serializers.ModelSerializer):

    student = serializers.StringRelatedField(read_only=True)

    course_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Review
        fields = ['id', 'student', 'course_id', 'rating', 'comment', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        course_id = validated_data.pop('course_id')

        course = Course.objects.get(id=course_id)

        review, created = Review.objects.update_or_create(
            student=user,
            course=course,
            defaults=validated_data
        )
        return review