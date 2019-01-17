from django.contrib.auth.models import User
from rest_framework import serializers

from Pieza.models import PiezaEje
from Pieza.models import PiezaResultado
from Pieza.models import Ejecucion
from Pieza.models import ResultadoGeneral
from Pieza.models import Fase
from Pieza.models import DatosInput

class EjecucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejecucion
        fields = ('id','fecha')

class PiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiezaEje
        fields = ('id','nPieza','ejecucion')
class ResultadoGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoGeneral
        fields = ('id','tiempoMax','tiempoMin','tiempoMedio','tiempoMin','SA','SR', 'NA', 'NR')
class PiezaResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiezaResultado
        fields = ('id','nPieza','ejecucion','tiempoEsperado','tiempoTotal', 'diferenciaAde', 'diferenciaRetra')

class FaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fase
        fields = ('id','nPieza', 'nPiezaEje','ejecucion', 'nFase','tiempoRequerido','maquinaNecesaria', 'tiempoFaseEntrada', 'tiempoFaseSalida', 'color', 'brightness')

class DatosInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosInput
        fields = ('id','ejecucion','nPiezaEje', 'nFase','tiempoRequerido','maquinaNecesaria','valor','tiempoEs' , 'index')

