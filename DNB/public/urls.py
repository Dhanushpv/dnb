from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('login',views.doLogin),
    path('logout',views.Logout),
    path('staff_register',views.staffreg),
    path('students_register',views.student),
    path('notifications',views.notifications),
    path('staff_view',views.staff_view),
    path('students_view',views.viewstudent),
    path('Department',views.departments),
    path('add_department',views.addepartment),
    path('add_semesters',views.addsem),
    path('semester',views.semester),
    path('subject',views.add_sub),
    path('subject_view',views.sub_views),

  
]
