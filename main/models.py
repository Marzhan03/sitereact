from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255, null=True)


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
