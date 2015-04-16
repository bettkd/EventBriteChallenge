from django.db import models

class Category(models.Model):
	event = models.CharField(max_length=140)
	description = models.TextField()
	address = models.TextField()
