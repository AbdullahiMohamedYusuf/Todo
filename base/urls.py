from django.contrib import admin
from django.urls import path, include
from .views import home, task,deletePage,login,signup,logout

urlpatterns = [
    #actual pages
    path('', home, name="home"),
    path('task', task, name="task"),
    #methods
    path('delete-page/<str:pk>', deletePage, name="delete"),

    #user
    path('login', login, name="login"),
    path('create-user', signup, name="create"),
    path('logout',logout, name="logout" )
]
