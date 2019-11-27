from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

class Currencies(models.Model):
    currency  = models.CharField(max_length=10)
    buying    = models.FloatField() 
    sales     = models.FloatField()
    diffrence = models.FloatField()
    code      = models.CharField(max_length=10)

def __str__(self):
    return self.currency


