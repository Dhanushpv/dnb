from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('Room',views.addroom),
path('Room_view',views.roomviews),
path('Add_exam',views.add_exam),
path('Exam_view',views.examview),
path('Classallocation',views.classaloc),
path('Classallocation_view',views.classview),


]