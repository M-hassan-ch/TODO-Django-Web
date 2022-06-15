from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Task(models.Model):
    status_choices = [
    ('C', 'COMPLETED'),
    ('P', 'PENDING'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2 , choices=status_choices)
    user  = models.ForeignKey(User  , on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)