from django.contrib import admin
# Register your models here.
from .models import *

@admin.register(College)
class CollegeDisplay(admin.ModelAdmin):
    list_display = ('id', 'collegeName', 'collegeAddress', 'collegeCity')

@admin.register(Course)
class CourseDisplay(admin.ModelAdmin):
    list_display = ('id', 'courseName', 'courseDuration', 'courseDescription')

@admin.register(Student)
class StudentDisplay(admin.ModelAdmin):
    list_display = ('id', 'Student_Name', 'college_Name')

@admin.register(Subject)
class SubjectDisplay(admin.ModelAdmin):
    list_display = ('id', 'subjectName', 'college_Name', 'course_Name')

