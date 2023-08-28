from django.urls import path
from . import views


#urlpattern is used by default for backwards compatibility 
urlpatterns = [
    path('tasks/', views.task_list, name='tasks'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
]
