from django.shortcuts import render
from .forms import *
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from public.models import Register
from django.contrib import auth
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request): 
    print("hiiiii")
    return render(request,'index.html')

def doLogin(request):
    form = LoginForm()
    if request.method == "POST":
        user = authenticate(request,username=request.POST["username"],password=request.POST["password"] )
        if user is None:
            return render(request,'login.html',{'form':form,'k':True})   
        else:
            login(request, user)
            data = Register.objects.get(username=user)
            request.session['ut']=data.usertype
            data.usertype
            request.session['userid']=data.id

            return redirect('/')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})


def Logout(request):
    auth.logout(request)
    return redirect('/')
def staffreg(request):
    form = staffform(request.POST,request.FILES)
    print(request.method)
    if request.method=="POST":
        
        Register.objects.create_user(
        username=request.POST['username'],
        email=request.POST['email'],
        password=request.POST['password'],
        gender=request.POST['gender'],
        date_of_birth=request.POST['date_of_birth'],
        contact=request.POST['contact'],
        address=request.POST['address'],
        qualification=request.POST['qualification'],
        department=request.POST['department'],
        experience=request.POST['experience'],
        usertype=1
        )
        return redirect('/staff_register')
    else:
        
        form = staffform()
        return render(request,'staff_register.html',{'form':form})


def student(request):
    form = studentform(request.POST,request.FILES)
    if request.method=="post":
        if form.is_valid():
            Register.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            gender=request.POST['gender'],
            date_of_birth=request.POST['date_of_birth'],
            contact=request.POST['contact'],
            address=request.POST['address'],
            register_number=request.POST['register_number'],
            # qualification=request.POST['qualification'],
            department=request.POST['department'],
            usertype=2
            # experience=request.POST['experience'],
            )
        return redirect('/students_register')
    else:
        form = studentform()
        return render(request,'students_register.html')

    # form = staff_register()
    # if request.method == "POST":
    #     user = authenticate(request,username=request.POST["username"],password=request.POST["password"] )
    #     if user is None:
    #         return render(request,'staff_register.html',{'form':form,'k':True})   
    #     else:
    #         login(request, user)
    #         data = Register.objects.get(username=user)
    #         request.session['ut']=data.usertype
    #         data.usertype
    #         request.session['userid']=data.id

    #         return redirect('/')
    # else:
    #     form = LoginForm()
    # return render(request,'staff_register.html',{'form':form})
   
def notifications(request):
    notfic="helloo"
    notifications.objects.create(
    message=notfic
    )
    return redirect('/')

def staff_view(request):
    staff=Register.objects.filter(usertype=2)
    return render(request,'staff_view.html',{'staff':staff})


def viewstudent(request):
    student=Register.objects.filter(usertype=0)
    return render(request,'students_view.html',{'student':student})


def departments(request):
    department= Departments.objects.all()
    return render(request,'Department.html',{'department':department})


def addepartment(request):
    form = departmentaddform(request.POST,request.FILES)
    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data['departmentname'])
            Departments.objects.create(
              departmentname=form.cleaned_data['departmentname'],
              description=form.cleaned_data['description']

            )
           
            return redirect('/add_department')
    else:
        form = departmentaddform()
        return render(request,'add_department.html',{'form':form})
    

def semester(request):
    semester= Semesters.objects.all()
    return render(request,'semester.html',{'semester':semester})    

def addsem(request):
    form = SemesterAddForm(request.POST,request.FILES)
    if request.method == "POST":
        if form.is_valid():
            Semesters.objects.create(
                department=form.cleaned_data['department'],
                semestername=form.cleaned_data['semestername']
            )
        return redirect('/')
    else:
        form = SemesterAddForm()
        return render(request,'add_semesters.html',{'form':form})

# def add_sub(request):
#     semester= Semesters.objects.all()
#     department= Departments.objects.all()
#     return render(request,'subject.html',{'semester':semester,'department':department})    

    
# def add_sub(request):
#     department= Departments.objects.all()
#     return render(request,'subject.html',{'department':department})

def add_sub(request):
    
    if request.method=="POST":
        
        Subjects.objects.create(
            department=Departments.objects.get(id=request.POST['depname']),
            semester=Semesters.objects.get(id=request.POST['semname']),
            subname=request.POST['subname']

        )
        return redirect('/subject')
        
    else:
        semester= Semesters.objects.all()
        department= Departments.objects.all()
        return render(request,'subject.html',{'semester':semester,'department':department})

def sub_views(request):
    sub=Subjects.objects.all()
    # print(rooms)
    return render(request,'subject_view.html',{'sub':sub})