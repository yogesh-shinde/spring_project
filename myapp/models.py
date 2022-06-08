from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    prof_name = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "course"


class Student(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name="student_course", null=True, blank=True)

    class Meta:
        db_table = "student"