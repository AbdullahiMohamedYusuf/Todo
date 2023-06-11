from django.forms import ModelForm
from .models import Todo
from django.contrib.auth.models import User


class Task(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

class SignUp(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
