from rest_framework import serializers
from . models import *


#create serializers
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','description','created_at','due_date','status']
        depth = 1