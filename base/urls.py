from django.contrib import admin
from django.urls import path, include
from .views import home, task,deletePage,create_user

urlpatterns = [
    path('', home, name="home"),
    path('task', task, name="task"),
    path('delete-page/<str:pk>', deletePage, name="delete"),
    path('create-user', create_user, name="create")
]
