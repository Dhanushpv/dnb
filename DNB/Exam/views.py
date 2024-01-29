from django.shortcuts import render
from .forms import *
from django.shortcuts import render,redirect
from public.models import *


# Create your views here.


def addroom(request):
    form = roomaddingform(request.POST,request.FILES)
    if request.method=="POST":  
        if form.is_valid():
            row=form.cleaned_data['row']
            column=form.cleaned_data['column']
            strength=row*column
            room.objects.create(
                roomname=form.cleaned_data['roomname'],
                row=row,
                column=column,
                strength=strength
             )
            return redirect('/Room')

    else:
        form = roomaddingform()
        return render(request,'Room.html',{'form':form})


def roomviews(request):
    rooms=room.objects.all()
    # print(rooms)
    return render(request,'Room_view.html',{'rooms':rooms})    


def add_exam(request):
    form = examform(request.POST,request.FILES)
    dep = Departments.objects.all()
    sem = Semesters.objects.all()
    sub = Subjects.objects.all()
    if request.method=="POST":
            exam.objects.create(
                department=Departments.objects.get(id=request.POST['depname']),
                subname=Subjects.objects.get(id=request.POST['subname']),
                semester=Semesters.objects.get(id=request.POST['semname']),
                examname=request.POST['examname'],
                date=request.POST['date'],
                starttime=request.POST['starttime'],
                endtime=request.POST['endtime'],
            )

            return redirect('/Add_exam')
      
    else:
        form = examform()
        dep=Departments.objects.all()
        sem=Semesters.objects.all()
        sub=Subjects.objects.all()

        return render(request,'Add_exam.html',{'form':form,'dep':dep ,'sem':sem ,'sub':sub})


def examview(request):
    exams=exam.objects.all()
    # print(rooms)
    return render(request,'Exam_view.html',{'exams':exams}) 


def classaloc(request):
    form = classalocform(request.POST,request.FILES)
    if request.method=="POST":  
        if form.is_valid():
            Class.objects.create(
                examname=exam.objects.get(id=request.POST['examname']),
                roomname=room.objects.get(id=request.POST['roomname']),




            )
                
            return redirect('/Classallocation')

    else: 
        form = classalocform()

        return render(request,'Classallocation.html',{'form':form})

def classview(request):
    classview=Class.objects.all()
    # print(rooms)
    return render(request,'Classallocation_view.html',{'classview':classview})     