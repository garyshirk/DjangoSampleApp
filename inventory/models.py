from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.IntegerField()
	backorder=models.IntegerField(default=0)

class Staff(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	division = models.CharField(max_length=200)
	timeonjob=models.IntegerField(default=0)
