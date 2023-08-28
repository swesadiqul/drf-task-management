from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    status = models.ForeignKey('TaskStatus', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class TaskStatus(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name


