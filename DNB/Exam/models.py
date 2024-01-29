from django.db import models
from django.db import models
from public.models import *


# Create your models here.



class room(models.Model):
    roomname=models.CharField(max_length=500,default='')
    row=models.IntegerField(null=True)
    column=models.IntegerField(null=True)
    strength=models.IntegerField(null=True)



class exam(models.Model):
    department = models.ForeignKey(Departments,on_delete=models.CASCADE,null=True)
    semester = models.ForeignKey(Semesters,on_delete=models.CASCADE,null=True)
    subname = models.ForeignKey(Subjects,on_delete=models.CASCADE,null=True)
    examname=models.CharField(max_length=500,default='')
    date=models.DateField(max_length=500,default='')
    starttime=models.TimeField(max_length=500,default='')
    endtime=models.TimeField(max_length=500,default='')


class Class(models.Model):
    examname=models.TimeField(max_length=500,default='')
    roomname=models.TimeField(max_length=500,default='')
   

