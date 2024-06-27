from django.db import models

# Create your models here.
from django.db import models

from  django.db import models
class Task(models.Model):
    id=models.AutoField(primary_key=True)
    head=models.CharField(max_length=50,verbose_name="Enter the Task ")
    desc=models.CharField(max_length=200,verbose_name="Enter the Description")
    #completed=models.BooleanField(default=False,verbose_name="Task Completed")
    def __str__(self):
        return str(self.head)

