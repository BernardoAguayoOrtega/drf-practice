from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
