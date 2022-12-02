from django.db import models

# Create your models here.


class Walido(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.name
