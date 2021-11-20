from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime
from django.conf import settings

# Create your models here.
class NewSubjects(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	name =models.CharField(max_length= 30)
	description = models.CharField(max_length=200)
	date_time = models.DateTimeField(auto_now_add=True)
class Data(models.Model):
	heading = models.CharField(max_length=500)
	subject = models.ForeignKey(NewSubjects, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now_add=True)
	paragraph = models.CharField(max_length=10000)
	pic =models.ImageField(null= True, blank=True,upload_to='blogimages/')
