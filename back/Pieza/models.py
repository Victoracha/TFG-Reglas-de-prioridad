

# Create your models here.
from django.db import models
"""from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())"""

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

    """class Meta:
        ordering = ('created',)"""
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return PiezaResultado.objects.create(**validated_data)

class ResultadoGeneral(models.Model):
    id=models.ForeignKey(Ejecucion, primary_key=True, on_delete=models.CASCADE)
    tiempoMax=models.FloatField()
    tiempoMin = models.FloatField()
    tiempoMedio = models.FloatField()
    SA = models.FloatField()
    SR = models.FloatField()
    NA = models.FloatField()
    NR = models.FloatField()
    def create(self, validated_data):

        return ResultadoGeneral.objects.create(**validated_data)

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