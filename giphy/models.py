from django.db import models

class Gif(models.Model):
    name = models.CharField(max_length=25)
    link = models.CharField(max_length=500, default=" ")

    def __str__(self) -> str:
        return self.name
