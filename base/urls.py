from django.contrib import admin
from django.urls import path, include
from .views import home, task,deletePage,login,signup

urlpatterns = [
    path('', home, name="home"),
    path('task', task, name="task"),
    path('delete-page/<str:pk>', deletePage, name="delete"),
    path('login', login, name="login"),
    path('create-user', signup, name="create")
]
