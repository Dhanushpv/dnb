from django import forms
from .models import *
# from department.models import *


        
class LoginForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ['username','password']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
            "password" : forms.PasswordInput(attrs={'class':'form-input','style':'width : 100%;'})
        }
        help_texts = {
            'username': None,
            'password': None,
        }

class staffform(forms.ModelForm):

    class Meta:
        model = Register
        fields = ['username','email','contact','gender','date_of_birth','address','experience','department','qualification','password']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
            "email" :forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
            "contact":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
            "gender":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
            "date_of_birth":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
            "address":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
            "experience":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
            "qualification":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
            "password":forms.PasswordInput(attrs={'class':'form-input','style':'width : 100%;'}),
            "department":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
        }

class studentform(forms.ModelForm):
    class Meta:
      model = Register
      fields = ['username','email','contact','gender','date_of_birth','address','password','register_number',]
      widgets ={
        "username" : forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
        "email" :forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
        "contact":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
        "gender":forms.Select(attrs={'class':'form-input','style':'width : 100%;'}),
        "date_of_birth":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
        # "address":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
        # "experience":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
        # "qualification":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
        # "register_number":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
        # "semester":forms.TextInput(attrs={'class':'form-input','style':'width : 100%;'}),
        "password":forms.PasswordInput(attrs={'class':'form-input','style':'width : 100%;'}),
    }    



class departmentaddform(forms.ModelForm):
    class Meta:
        model = Departments
        fields = "__all__"
        widgets = {
            'description' : forms.Textarea(attrs={'class':'contact-input'}),
            'departmentname' : forms.TextInput(attrs={'class':'contact-input'})
        }


class SemesterAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].widget.attrs['class'] = 'custom-select'
    class Meta:
        model = Semesters
        fields = ['department','semestername']
        widgets = {
            'semestername' : forms.TextInput(attrs={'class':'contact-input'})
        }   



        