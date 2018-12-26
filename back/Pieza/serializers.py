from django.contrib.auth.models import User
from rest_framework import serializers

from Pieza.models import PiezaEje
from Pieza.models import Ejecucion
class EjecucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejecucion
        fields = ('id','fecha')

class PiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiezaEje
        fields = ('id','nPieza','ejecucion')
