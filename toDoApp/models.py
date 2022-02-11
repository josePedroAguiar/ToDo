from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField(blank=True,max_length=1000)
    created = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True,blank=True)
    date= models.DateTimeField(null=True,blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User , on_delete= models.CASCADE)

    def __str__(self):
        return self.title