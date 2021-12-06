from django.db import models


class Book(models.Model):
    author = models.CharField(
        max_length=40,
    )
    titile = models.CharField(
        max_length=30,
    )
    description = models.TextField()
    pages = models.PositiveIntegerField()
