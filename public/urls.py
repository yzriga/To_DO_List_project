from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('tasks/', views.task_list_view, name='tasks'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/mark/<int:task_id>/', views.mark_task, name='mark_as_finished'),
    path('tasks/mark/<int:task_id>/', views.mark_task, name='mark_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('', views.home_view, name='home'),
]
