from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Pieza.models import PiezaEje
from Pieza.serializers import PiezaSerializer
from Pieza.models import Ejecucion
from Pieza.serializers import EjecucionSerializer
@csrf_exempt
def ejecucion_list(request):

    if request.method == 'GET':
        ejecucion= Ejecucion.objects.all()
        serializer = EjecucionSerializer(ejecucion, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def pieza_list(request):

    if request.method == 'GET':
        piezas= PiezaEje.objects.all()
        serializer = PiezaSerializer(piezas, many=True)
        return JsonResponse(serializer.data, safe=False)
