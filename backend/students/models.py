from django.db import models


class User(models.Model):

    ROLE_CHOICES = (
        ('HOD','HOD'),
        ('TEACHER','TEACHER'),
        ('STUDENT','STUDENT')
    )

    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)




class Student(models.Model):

    YEAR = (
        ('1','1st Year'),
        ('2','2nd Year'),
        ('3','3rd Year'),
        ('4','4th Year'),
    )

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    marks = models.IntegerField()

    cgpa = models.FloatField(default=0)
    attendance = models.IntegerField(default=0)
    performance = models.CharField(max_length=50, default="Good")

    year = models.CharField(max_length=10, choices=YEAR)

    created_by = models.CharField(max_length=50)

    image = models.ImageField(upload_to="students/", null=True, blank=True)
    