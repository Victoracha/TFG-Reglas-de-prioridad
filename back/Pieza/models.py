

# Create your models here.
from django.db import models


class Ejecucion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    nPiezas= models.IntegerField()
    nMaquinas= models.IntegerField()
    def create(self, validated_data):

        return Ejecucion.objects.create(**validated_data)

class PiezaEje(models.Model):
    id=models.AutoField(primary_key=True )
    nPieza = models.IntegerField()
    ejecucion = models.ForeignKey(Ejecucion, on_delete=models.CASCADE)
    """class Meta:
        ordering = ('created',)"""
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return PiezaEje.objects.create(**validated_data)

class PiezaResultado(models.Model):
    id=models.AutoField(primary_key=True )
    nPieza = models.IntegerField()
    ejecucion = models.ForeignKey(Ejecucion, on_delete=models.CASCADE)
    tiempoEsperado = models.FloatField()
    tiempoTotal = models.FloatField()
    diferenciaAde = models.FloatField()
    diferenciaRetra = models.FloatField()
    indiceResultado = models.IntegerField()
    algoritmo = models.CharField(max_length=50)
    """class Meta:
        ordering = ('created',)"""
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return PiezaResultado.objects.create(**validated_data)

class ResultadoGeneral(models.Model):
    id=models.AutoField(primary_key=True)
    tiempoMax=models.FloatField()
    tiempoMin = models.FloatField()
    tiempoMedio = models.FloatField()
    SA = models.FloatField()
    SR = models.FloatField()
    NA = models.FloatField()
    NR = models.FloatField()
    ejecucion = models.ForeignKey(Ejecucion, on_delete=models.CASCADE)
    algoritmo = models.CharField(max_length=50)
    def create(self, validated_data):

        return ResultadoGeneral.objects.create(**validated_data)

class ResultadoFinal(models.Model):
    id = models.AutoField(primary_key=True)
    tiempoMax=models.FloatField()
    tiempoMin = models.FloatField()
    tiempoMedio = models.FloatField()
    SA = models.FloatField()
    SR = models.FloatField()
    NA = models.FloatField()
    NR = models.FloatField()
    ejecucion = models.ForeignKey(Ejecucion, on_delete=models.CASCADE)
    algoritmo = models.CharField(max_length=50)
    def create(self, validated_data):

        return ResultadoFinal.objects.create(**validated_data)

class Fase(models.Model):
    id=models.AutoField(primary_key=True )
    nPieza=models.ForeignKey(PiezaResultado, on_delete=models.CASCADE)
    nPiezaEje=models.IntegerField()
    ejecucion = models.ForeignKey(Ejecucion, on_delete=models.CASCADE)
    nFase = models.IntegerField()
    tiempoRequerido = models.FloatField()
    maquinaNecesaria = models.IntegerField()
    tiempoFaseEntrada = models.FloatField()
    tiempoFaseSalida = models.FloatField()
    color = models.IntegerField()
    brightness= models.FloatField()
    indiceResultado = models.IntegerField()
    tiempoMax = models.IntegerField()
    def create(self, validated_data):

        return ResultadoGeneral.objects.create(**validated_data)
class DatosInput(models.Model):
    id =models.AutoField(primary_key=True )
    ejecucion=models.ForeignKey(Ejecucion, on_delete=models.CASCADE)
    nPiezaEje = models.IntegerField()
    nFase = models.IntegerField()
    tiempoRequerido = models.FloatField()
    maquinaNecesaria = models.IntegerField()
    valor = models.IntegerField()
    tiempoEs = models.FloatField()
    index = models.IntegerField()

    def create(self, validated_data):

        return DatosInput.objects.create(**validated_data)
"""class MaquinaResultado(models.Model):
    id=models.ForeignKey(Ejecucion, primary_key=True, on_delete=models.CASCADE)
    =models.FloatField()
    tiempoMin = models.FloatField()
    tiempoMedio = models.FloatField()
    SA = models.FloatField()
    SR = models.FloatField()
    NA = models.FloatField()
    NR = models.FloatField()
    def create(self, validated_data):

        return ResultadoGeneral.objects.create(**validated_data)"""