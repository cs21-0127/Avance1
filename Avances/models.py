from django.db import models

# Create your models here.
class producto (models.Model):
    codigoProducto = models.CharField(max_length=10)
    descripcionProducto = models.CharField(max_length=225)
    estatus = models.BooleanField()