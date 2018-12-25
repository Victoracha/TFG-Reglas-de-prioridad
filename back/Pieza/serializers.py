from django.contrib.auth.models import User
from rest_framework import serializers

from Pieza.models import Pieza
class PiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pieza
        fields = ('id','nPieza')
