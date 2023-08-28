from django.contrib import admin
from .models import Task, TaskStatus

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskStatus)

