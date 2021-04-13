from django.db import models


# Create your models here.
# class Role(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#
#
#
#     class Meta:
#         db_table = "SOS_ROLE"

#
# class User(models.Model):
#     firstName = models.CharField(max_length=50)
#     lastName = models.CharField(max_length=50)
#     login_id = models.EmailField()
#     password = models.CharField(max_length=20)
#     confirmpassword = models.CharField(max_length=20, default='')
#     dob = models.DateField(max_length=20)
#     address = models.CharField(max_length=50, default='')
#     gender = models.CharField(max_length=50, default='')
#     mobilenumber = models.CharField(max_length=50, default='')
#     role_Id = models.IntegerField()
#     role_Name = models.CharField(max_length=50)
#
#     # role_ID=models.IntegerField()
#
#     class Meta:
#         db_table = "SOS_USER"
#

class College(models.Model):
    collegeName = models.CharField(max_length=50)
    collegeAddress = models.CharField(max_length=50)
    collegeState = models.CharField(max_length=50)
    collegeCity = models.CharField(max_length=20)
    collegePhoneNumber = models.CharField(max_length=20)

    def __str__(self):
        return self.collegeName

    class Meta:
        db_table = "SOS_COLLEGE"




class Course(models.Model):
    courseName = models.CharField(max_length=50)
    courseDescription = models.CharField(max_length=100)
    courseDuration = models.CharField(max_length=100)
    collegeName = models.ForeignKey(College, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.courseName

    class Meta:
        db_table = "SOS_COURSE"


# class Faculty(models.Model):
#     firstName = models.CharField(max_length=50)
#     lastName = models.CharField(max_length=50)
#     email = models.EmailField()
#     password = models.CharField(max_length=20)
#     mobileNumber = models.CharField(max_length=20)
#     address = models.CharField(max_length=50)
#     gender = models.CharField(max_length=50)
#     dob = models.DateField(max_length=20)
#     college_ID = models.IntegerField()
#     # collegeName = models.CharField(max_length=50)
#     subject_ID = models.IntegerField()
#     # subjectName = models.CharField(max_length=50)
#     course_ID = models.IntegerField()
#
#     # courseName = models.CharField(max_length=50)
#
#
#     class Meta:
#         db_table = "SOS_FACULTY"


# class Marksheet(models.Model):
#     rollNumber = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     physics = models.IntegerField()
#     chemistry = models.IntegerField()
#     maths = models.IntegerField()
#
#     class Meta:
#         db_table = "SOS_MARKSHEET"


class Student(models.Model):
    Student_Name = models.CharField(max_length=50)
    dob = models.DateField(max_length=20)
    mobile_Number = models.CharField(max_length=20)
    email = models.EmailField()
    college_Name = models.ForeignKey(College, on_delete=models.CASCADE)


    class Meta:
        db_table = "SOS_STUDENT"


class Subject(models.Model):
    subjectName = models.CharField(max_length=50)
    subjectDescription = models.CharField(max_length=50)
    course_Name = models.ForeignKey(Course, on_delete=models.CASCADE)
    college_Name = models.ForeignKey(College, on_delete=models.CASCADE)

    class Meta:
        db_table = "SOS_SUBJECT"


# class TimeTable(models.Model):
#     examTime = models.CharField(max_length=40)
#     examDate = models.DateField()
#     subject_ID = models.IntegerField()
#     course_ID = models.IntegerField()
#     semester = models.CharField(max_length=50)
#
#     class Meta:
#         db_table = "SOS_TIMETABLE"
