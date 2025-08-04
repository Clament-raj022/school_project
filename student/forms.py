from django import forms
from student.models import *
class Login_form(forms.ModelForm):
    class Meta:
        model=Login_model
        fields='__all__'

# Student Registration Form

class stud_registration_form(forms.ModelForm):
    class Meta:
        model=stud_registration_model
        fields="__all__"
        # widget={'password':forms.PasswordInput(),
                # 'date_of_birth':forms.DateInput(attrs={'type':'date'})
                # }
        
class registration_form(forms.ModelForm):
    class Meta:
        model=registration_model
        fields="__all__"

class student_marks_register_form(forms.ModelForm):
    class Meta:
        model=student_marks_register_model
        fields="__all__"