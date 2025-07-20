from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Site(models.Model):
    site_name        = models.CharField(max_length=50, blank=True, null=True)
    address          = models.CharField(max_length=50, blank=True, null=True)
    link             = models.URLField(max_length=200, blank=True, null=True)
    site_image       = models.ImageField(upload_to='images/', blank=True, null=True)
    manager          = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.site_name

class Location(models.Model):
    code             = models.CharField(max_length=12, blank=True, null=True)
    area             = models.ImageField(upload_to='images/',blank=True, null=True)
    location         = models.ImageField(upload_to='images/',blank=True, null=True)
    additional       = models.ImageField(upload_to='images/', blank=True, null=True)
    site             = models.ForeignKey(Site,blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.code

class Task(models.Model):
    task_name        = models.TextField(blank=True, null=True)
    starting_date    = models.DateField(auto_now=False, auto_now_add=False,blank=True, null=True)
    location          = models.ForeignKey(Location,blank=True, null=True, on_delete=models.CASCADE)
    #operators       = models.ManyToManyField(Team,blank=True)
    def __str__(self):
        return self.task_name


class Team(models.Model):
    name                = models.CharField(max_length=50, blank=True, null=True)
    phone_number        = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    email               = models.EmailField(max_length=254,blank=True, null=True)
    task                = models.ManyToManyField(Task, blank=True, null=True)
    def __str__(self):
        return self.name










