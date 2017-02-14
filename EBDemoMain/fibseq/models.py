from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Element(models.Model):
	value = models.IntegerField()
	position = models.IntegerField()

	def __str__(self):
		return "{:03d} element of Fib seq: {}".format(self.position, self.value)