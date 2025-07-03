from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year_graduated = models.IntegerField(max_length=4)
    linkedin_profile = models.URLField(max_length=200, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)   
    start_employment_date = models.DateField(blank=True, null=True)
    end_employment_date = models.DateField(blank=True, null=True)
    