from django.db import models

# Create your models here.

class Task(models.Model):
    pub_date = models.DateTimeField('date published')
    desc = models.CharField(max_length = 200)
    assignee = models.CharField(max_length = 200)
    supervisor = models.CharField(max_length = 200)
    due_date = models.DateTimeField('date published')
    priority = models.IntegerField(default=1)
    
