from django.db import models

class Courses(models.Model):
	crn = models.CharField(max_length=64)
	crsnum = models.CharField(max_length=64)
	title = models.CharField(max_length=64)
	credits = models.CharField(max_length=64)
	day = models.CharField(max_length=64)
	start = models.CharField(max_length=64)
	end = models.CharField(max_length=64)
	building = models.CharField(max_length = 64)
	room = models.CharField(max_length = 64)
	cap = models.CharField(max_length = 64)
	prof = models.CharField(max_length = 64)
	current = models.CharField(max_length = 64)
