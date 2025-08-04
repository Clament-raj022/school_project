from django.db import models
from datetime import date
import random


# Create your models here.
class Login_model(models.Model):
    UserName=models.CharField( max_length=50)
    Password=models.CharField( max_length=50)
    chc=[("Teacher","Teacher"),("Student","Student"),("Admin","Admin")]
    Member=models.CharField(max_length=50, choices=chc)
    class Meta:
        db_table='Login Form'
        
        
        
# Student Registration

class stud_registration_model(models.Model):
    id=models.AutoField(primary_key=True)
    cls=[("6th" ,"6th"),("7th","7th"),("8th","8th"),("9th","9th"),("10th","10th"),("11th","11th"),("12th","12th")]
    name=models.CharField( max_length=50)
    Clas=models.CharField( max_length=50,choices=cls)
    date_of_birth=models.DateField(default=date.today,editable=True,null=True)
    mail=models.CharField( max_length=50)
    mobile=models.CharField( max_length=10)
    address=models.CharField(max_length=100)
    
    
    your_reister_no_is=models.CharField(max_length=10,null=True)
    
    profile=models.FileField(null=True)
    date=models.DateField(default=date.today,editable=False)
    status=models.IntegerField(default=1,editable=False)
    class Meta:
        db_table='student_registration'

# Create your models here.
class registration_model(models.Model):
    id=models.AutoField(primary_key=True)
    teacher_name=models.CharField( max_length=50,null=True)
    mail=models.CharField( max_length=50,null=True)
    mobile=models.CharField( max_length=10,null=True)
    address=models.CharField( max_length=100,null=True)
    cnt=[("India" ,"India"),("USA","America"),("other","Other")]
    country=models.CharField( max_length=50,choices=cnt)
    profile=models.FileField(null=True)
    date=models.DateField(default=date.today,editable=False)
    status=models.IntegerField(default=1,editable=False)
    class Meta:
        db_table='teacher_registration'

# Student Marks Register
class student_marks_register_model(models.Model):
    id=models.AutoField(primary_key=True)
    stu_id=models.IntegerField(null=True)
    tamil=models.IntegerField(null=True)
    english=models.IntegerField(null=True)
    maths=models.IntegerField(null=True)
    science=models.IntegerField(null=True)
    social=models.IntegerField(null=True)
    # total=models.IntegerField(null=True)
    # percentage=models.IntegerField(null=True)
    date=models.DateField(default=date.today,editable=False)
    status=models.IntegerField(default=1,editable=False)
    class Meta:
        db_table='student_marks_register'
    
    

    