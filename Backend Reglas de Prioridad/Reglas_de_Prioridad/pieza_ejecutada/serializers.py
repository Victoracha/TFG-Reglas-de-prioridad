from django.shortcuts import render

from rest_framework import serializers
from .models import PiezaEjecucion

class PiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiezaEjecucion
        fields = "__all__"