from __future__ import unicode_literals
from django import forms 
from django.db import models 


class Item(models.Model):
	itemtodo = models.CharField(max_length=200, null=True)
	done = models.BooleanField(default=False)
	date = models.DateField(auto_now_add=True, blank=False)
	findate = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return self.itemtodo 

