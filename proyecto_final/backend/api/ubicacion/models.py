from django.db import models


class Region(models.Model):
    descripcion = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)


class Comuna(models.Model):
    descripcion = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
