from django.db import models


class PiezaEjecucion(models.Model):
    nPieza = models.IntegerField(primary_key=True)

class MaquinaEjecucion(models.Model):
    nMaquina=models.IntegerField(primary_key=True)

class FaseEjecucion(models.Model):
    nFase = models.IntegerField(primary_key=True)
    tiempoRequerido = models.FloatField
    maquinaNecesaria = models.ForeignKey(MaquinaEjecucion, on_delete=models.CASCADE)
    nPieza = models.ForeignKey(PiezaEjecucion, on_delete=models.CASCADE)




class Maquinas_Ejecutadas(models.Model):

    maquinaNecesaria = models.ForeignKey(MaquinaEjecucion, on_delete=models.CASCADE, primary_key=True)
    nFase = models.ForeignKey(FaseEjecucion, on_delete=models.CASCADE)
    nPieza = models.ForeignKey(PiezaEjecucion, on_delete=models.CASCADE)
    orden= models.IntegerField
    tiempoRequerido = models.FloatField