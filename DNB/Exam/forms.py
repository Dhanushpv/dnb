from django import forms
from .models import *



class roomaddingform(forms.ModelForm):
    class Meta:
        model=room
        fields=['roomname','row','column']
        widgets={
            "roomname":forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "row":forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
            "column":forms.TextInput(attrs={'class':'form-input','style':'width : 90%;'}),
        }

class examform(forms.ModelForm):
    # departmentname = forms.ModelChoiceField(queryset=Departments.objects.all())
    # semestername = forms.ModelChoiceField(queryset=Semesters.objects.all())

    class Meta:
        model = exam
        fields = ['examname','date','starttime','endtime']
        widgets = {
            
            "examname": forms.TextInput(attrs={'class': 'form-input', 'style': 'width : 90%;'}),
            "date": forms.TextInput(attrs={'class': 'form-input', 'style': 'width : 90%;'}),
            "starttime": forms.TextInput(attrs={'class': 'form-input', 'style': 'width : 90%;'}),
            "endtime": forms.TextInput(attrs={'class': 'form-input', 'style': 'width : 90%;'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(examform, self).__init__(*args, **kwargs)
    #     self.fields['semestername'].widget.attrs.update({'data-did': ''})


class classalocform(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['roomname','examname']
        widgets = {
            "roomname": forms.TextInput(attrs={'class': 'form-input', 'style': 'width : 90%;'}),
            "examname": forms.TextInput(attrs={'class': 'form-input', 'style': 'width : 90%;'}),

            
           
        }
