from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class Register(AbstractUser):
  
    experience=models.CharField(max_length=50,default='')
    qualification=models.CharField(max_length=50,default='')
    department=models.CharField(max_length=50,default='')
    date_of_birth=models.CharField(max_length=50,default='')
    Exam_status=models.CharField(max_length=50,default='0')
    Stauts=models.CharField(max_length=50,default='0')
    contact=models.CharField(max_length=50,default='0')
    address=models.CharField(max_length=50,default='0')
    gender=models.CharField(max_length=50,default='0')
    register_number=models.CharField(max_length=50,default='0')
    semester=models.CharField(max_length=50,default='0')
    usertype=models.IntegerField(null=True)

class notification(models.Model):
    Message=models.CharField(max_length=50,default='')
    Date=models.CharField(max_length=50,default='')
    Start_date=models.CharField(max_length=50,default='')
    End_date=models.CharField(max_length=50,default='')

# class department(models.Model):

class Departments(models.Model):
    departmentname = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=200,default='')
    def __str__(self) -> str:
        return self.departmentname


class Semesters(models.Model):
    semestername = models.CharField(max_length=100)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.semestername
    
class Subjects(models.Model):
    subname = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=500,default='')
    department = models.ForeignKey(Departments,on_delete=models.CASCADE,null=True)
    semester = models.ForeignKey(Semesters,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.name      
