from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Pieza.models import PiezaEje
from Pieza.serializers import PiezaSerializer
from Pieza.models import Ejecucion
from Pieza.serializers import EjecucionSerializer
from Pieza.models import ResultadoGeneral
from Pieza.serializers import ResultadoGeneralSerializer
from Pieza.models import Fase
from Pieza.serializers import FaseSerializer
from Pieza.models import PiezaResultado
from Pieza.serializers import PiezaResultadoSerializer
from algoritmos.Control import Control
import pdb
@csrf_exempt
def ejecucion_list(request):

    if request.method == 'GET':
        ejecucion= Ejecucion.objects.all()
        serializer = EjecucionSerializer(ejecucion, many=True)

        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        piezas_maquina = [[2, 3, 1], [2, 1, 2, 3], [3, 1, 2], [2, 3, 1, 2], [3, 2]]
        piezas_tiempo = [[2, 2, 1], [0.5, 2, 0.5, 2.5], [1.5, 2.5, 1], [1, 2.5, 3, 1], [0.5, 2]]
        tiempo=[]
        maquina=[]
        for pieza in data:
            print("id")
            print(pieza['id'])
            print("maquinas")
            print(pieza['maquinas'])
            print("tiempos")
            print(pieza['tiempos'])
            tiempo.append(pieza['tiempos'])
            maquina.append(pieza['maquinas'])
        print(data)
        print("maquina")
        print(maquina)
        print("tiempo")
        print(tiempo)
        control = Control(maquina, tiempo)
        #control = Control(piezas_maquina, piezas_tiempo)
        control.algoritmo()
        serializer = EjecucionSerializer(data=data)

        if serializer.is_valid():
            #serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def pieza_list(request):

    if request.method == 'GET':
        piezas= PiezaEje.objects.all()
        serializer = PiezaSerializer(piezas, many=True)
        return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def resultado_list(request):

    if request.method == 'GET':
        resultado= ResultadoGeneral.objects.all()
        serializer = ResultadoGeneralSerializer(resultado, many=True)
        return JsonResponse(serializer.data, safe=False)

def resultado_list_detail(request, pk):

    if request.method == 'GET':
        resultado= ResultadoGeneral.objects.get(pk=pk)
        serializer = ResultadoGeneralSerializer(resultado)
        return JsonResponse(serializer.data)

def fase_list_detail(request, ejecucion):

    if request.method == 'GET':
        resultado= Fase.objects.filter(ejecucion=ejecucion)
        serializer = FaseSerializer(resultado, many=True)
        return JsonResponse(serializer.data, safe=False)

def pieza_resultado_list_detail(request, ejecucion):

    if request.method == 'GET':
        resultado= PiezaResultado.objects.filter(ejecucion=ejecucion)
        serializer = PiezaResultadoSerializer(resultado, many=True)
        return JsonResponse(serializer.data, safe=False)

