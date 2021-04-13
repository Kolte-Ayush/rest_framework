from abc import ABC, ABCMeta

from rest_framework import serializers
from .models import College, Course, Student, Subject


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'





class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    collegeName = serializers.ReadOnlyField(source='college_Name.collegeName')

    class Meta:
        model = Student
        fields = ('id', 'Student_Name', 'dob', 'mobile_Number', 'email', 'collegeName')


class SubjectSerializer(serializers.ModelSerializer):
    collegeName = serializers.ReadOnlyField(source='college_Name.collegeName')
    courseName = serializers.ReadOnlyField(source='course_Name.courseName')

    class Meta:
        model = Subject
        fields = ('id', 'subjectName', 'subjectDescription', 'collegeName', 'courseName')
