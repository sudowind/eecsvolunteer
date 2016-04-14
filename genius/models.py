from __future__ import unicode_literals

from django.db import models
from django import forms


# Create your models here.

class Activity(models.Model):
    date = models.IntegerField()
    place = models.CharField(max_length=45, null=True)


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
