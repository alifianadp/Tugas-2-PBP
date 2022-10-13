from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, add_task, change_status, delete_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='add_task'),
    path('change-status/', change_status, name='change_status'),
    path('delete-task/', delete_task, name='delete_task'),
]