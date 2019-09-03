from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.http import HttpResponse
from user.models import User
# Create your models here.
class Job(models.Model):
	job_name= models.CharField(max_length=50)
	area= models.CharField(max_length=50)
	coordinate_system=models.CharField(max_length=50)
	antenna_serial_no=models.CharField(max_length=50)
	receiver_serial_no=models.CharField(max_length=50)
	date=models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('surveyorportal:detail', kwargs={'pk': self.pk})
	def __str__(self):
		return self.job_name +' - ' + self.area

class Files(models.Model):
	job= models.ForeignKey(Job, on_delete=models.CASCADE)
	observation_file= models.FileField(upload_to='obs_file/')
	coordinate_file=models.FileField()
	adjustment_vector_files=models.FileField()
	surveyor_report=models.FileField()
	observer_name=models.CharField(max_length=50)

	def get_absolute_url(self):
		return reverse('surveyorportal:index')

	def __str__(self):
		return self.observer_name

class Profile(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	lic_surveyor_name= models.CharField(max_length=50)
	surveyor_name= models.CharField(max_length=50)
	company_name=models.CharField(max_length=50)
	office_tel_no=models.IntegerField()
	phone_no=models.IntegerField()

	def __unicode__(self):
		return self.surveyor_name

class Settings(models.Model):
	update_profile=models.CharField(max_length=50)




