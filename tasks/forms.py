# forms.py
from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'is_complete']


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "username": "Username",
            "email": "Email",
            "password1": "Password",
            "password2": "Confirm  Password",
        }

        for field in self.fields:
            if field in placeholders:
                self.fields[field].widget.attrs["placeholder"] = placeholders[field]
    
    def clean_user(self):
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username=username)
        if new.count():
            raise forms.ValidationError('User  already exist')
        return  username
        password1 = self.cleaned_data['password1']    
    
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower() 
        newemail = User.objects.filter(email=email)
        if newemail.count():
            raise forms.ValidationError('Email  already exist')
        return email
                 
                 
    def clean_password2(self):
        password1 = self.cleaned_data['password1'] 
        password2 = self.cleaned_data['password2'] 
       
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Password  don't match")
        return password2     