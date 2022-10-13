from django.urls import path
from todolist.views import add_task_ajax, show_todolist, register, login_user, logout_user, add_task, change_status, delete_task, show_todolist_ajax, show_todolist_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='add_task'),
    path('change-status/', change_status, name='change_status'),
    path('delete-task/', delete_task, name='delete_task'),
    # Tugas 6 : AJAX
    path('json/', show_todolist_json, name='show_todolist_json'),
    path('ajax/', show_todolist_ajax, name='show_todolist_ajax'),
    path('add/', add_task_ajax, name='add_task_ajax')
]