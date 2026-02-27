from django.db import models
from django.conf import settings
from courses.models import Course, Lecture

User = settings.AUTH_USER_MODEL


# student enrollment
class Enrollment(models.Model):

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} - {self.course}"


# lecture progress tracking
class LectureProgress(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.enrollment} - {self.lecture}"