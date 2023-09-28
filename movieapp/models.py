from django.db import models

# Create your models here.

class Movie(models.Model):
    # id implicitly created
    title = models.CharField(max_length=250)
    year = models.IntegerField()
