
from django.shortcuts import render
from rest_framework import generics
from .models import PiezaEjecucion
from .serializers import PiezaSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.

class ContactListAPIView(generics.ListCreateAPIView):
    queryset = PiezaEjecucion.objects.all()
    serializer_class = PiezaSerializer
    #permission_classes = (IsAdminUser,