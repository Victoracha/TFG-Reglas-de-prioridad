from django.db import models

class PiezaEjecucion(models.Model):
    nPieza = models.IntegerField(primary_key=True)