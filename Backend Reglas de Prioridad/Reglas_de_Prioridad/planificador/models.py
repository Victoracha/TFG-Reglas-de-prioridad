from django.db import models


class Pieza(models.Model):
    nPieza = models.IntegerField(primary_key=True)

class Maquina(models.Model):
    nMaquina=models.IntegerField(primary_key=True)

class Fase(models.Model):
    nFase = models.IntegerField(primary_key=True)
    tiempoRequerido = models.FloatField
    maquinaNecesaria = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    nPieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)




class Maquinas_Ejecutadas(models.Model):

    maquinaNecesaria = models.ForeignKey(Maquina, on_delete=models.CASCADE, primary_key=True)
    nFase = models.ForeignKey(Fase, on_delete=models.CASCADE)
    nPieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    orden= models.IntegerField
    tiempoRequerido = models.FloatField