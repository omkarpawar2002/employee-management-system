from django import forms
from .models import Employee

gender_choices = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER'),
]

dept_choices = [
    # ('','Please Choose One'),
    ('IT','IT'),
    ('ADMIN','ADMIN'),
    ('SALES','SALES'),
    ('EXECUTIVE','EXECUTIVE'),
    ('FINANCE','FINANCE'),
]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'eid':'EMPLOYEE ID',
            'first_name':'FIRST NAME',
            'last_name':'LAST NAME',
            'mobile':'MOBILE NO',
            'gender':'GENDER',
            'city':'CITY',
            'address':'ADDRESS',
            'dept':'DEPARTMENT',
            'email':'EMAIL ID',
            'password':'PASSWORD',
            'eligible':'ELIGIBILITY'
        }
        widgets = {
            'eid':forms.TextInput(attrs={
                'placeholder':'101',
                'required':True
            }),
            'first_name':forms.TextInput(attrs={
                'placeholder':'Enter First Name',
                'required':True
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Enter Last Name',
                'required':True
            }),
            'mobile':forms.TextInput(attrs={
                'placeholder':'+91 **********'
            }),
            'gender':forms.RadioSelect(choices=gender_choices),
            'city':forms.TextInput(attrs={
                'placeholder':'E.g.,Mumbai'
            }),
            'address':forms.Textarea(attrs={
                'placeholder':'E.g.,Mumbai, Maharashtra',
                'rows':'3'
            }),
            'dept':forms.Select(choices=dept_choices),
            'email':forms.TextInput(attrs={
                'placeholder':'youremail@gmail.com',
                'required':True
            }),
            'password':forms.PasswordInput(attrs={
                'placeholder':'********',
                'required':True
            }),
            'eligible':forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
    