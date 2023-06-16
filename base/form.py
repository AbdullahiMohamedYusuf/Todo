from django.forms import ModelForm
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class Task(ModelForm):
    class Meta:
        model = Todo
        fields = ("topics", "task", "body")

class SignUp(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields =("username", "email", "password", "password2")


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
		
    
    