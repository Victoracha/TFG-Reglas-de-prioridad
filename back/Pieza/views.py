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
from django.utils import timezone
from Pieza.models import DatosInput
from Pieza.serializers import DatosInputSerializer
from Pieza.models import ResultadoFinal
from Pieza.serializers import ResultadoFinalSerializer

import pdb
@csrf_exempt
def ejecucion_list(request):

    if request.method == 'GET':
        ejecucion= Ejecucion.objects.all()
        serializer = EjecucionSerializer(ejecucion, many=True)

        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        piezas_maquina = [[2, 3, 1], [2, 1, 2, 3], [3, 1, 2], [2, 3, 1, 2], [3, 2]]
        piezas_tiempo = [[2, 2, 1], [0.5, 2, 0.5, 2.5], [1.5, 2.5, 1], [1, 2.5, 3, 1], [0.5, 2]]

        piezas_maquina = [[2, 3, 1], [2, 1, 2, 3], [3, 1, 2], [2, 3, 1, 2], [3, 2]]
        piezas_tiempo = [[1, 2, 1], [0.5, 2, 0.5, 2.5], [1.5, 2.5, 1], [1, 2.5, 3, 1], [0.5, 2]]

        nMaquinas=3
        """PRUEBAS"""
        #1
        piezas_maquina =[[2,3,4,1,2], [2,1,3,2,4],[3,4,2,1,2,1],[1,3,4,1]]
        nMaquinas=4
        piezas_tiempo =[[0.5,1,3,1.5,1], [2,0.5,1,2.5,1],[1,2,1.5,1,0.5,0.5],[2.5,1,3,0.5]]

        #2
        piezas_maquina = [[2,1 ,2 ], [1,2 ,1 ,2], [2,3 ,1], [2, 1, 2,1], [1,3,2]]
        nMaquinas = 3
        piezas_tiempo = [[0.5,1.5 ,1 ], [0.5, 1,0.5 ,1], [1,0.5 ,1.5], [1.5, 2, 1,0.5], [1, 1,0.5]]

        #3
        piezas_maquina = [[2, 3, 1], [2, 1, 2, 3], [3, 1, 2], [2, 3, 1, 2], [3, 2]]
        piezas_tiempo = [[1, 2, 1], [0.5, 2, 0.5, 2.5], [1.5, 2.5, 1], [1, 2.5, 3, 1], [0.5, 2]]
        tiempo=[]
        maquina=[]
        valores=[]
        tiempoEsperado=[]
        controlFallo=False
        print("DAATTAS")
        print(data[0])
        for pieza in data[0]:

            if len(pieza['maquinas'])==0:
                controlFallo=True

            print("id")
            print(pieza['id'])
            print("maquinas")
            print(pieza['maquinas'])
            print("tiempos")
            print(pieza['tiempos'])
            tiempo.append(pieza['tiempos'])
            maquina.append(pieza['maquinas'])
            for maqui in pieza['maquinas']:
                if nMaquinas<maqui:
                    nMaquinas=maqui
            valores.append(pieza['valor'])
            tiempoEsperado.append(pieza['tiempoEsperado'])
        print(data)
        print("maquina")
        print(maquina)
        print("tiempo")
        print(tiempo)
        #control = Control(maquina, tiempo)
        print(len(data[1]))
        #valores = [4, 3, 2, 5, 6]
        #tiempoEsperado = [6, 9, 6, 12, 5]
        indice=0
        print(len(piezas_maquina))
        nPiezas=len(data[0])
        if len(tiempo) >0 and len( maquina)>0 and len(data[1])>0:
            e = Ejecucion(fecha=timezone.now(), nPiezas=nPiezas, nMaquinas=nMaquinas)
            e.save()
            i=0
            for elemento in data[1]:
                #control = Control(piezas_maquina, piezas_tiempo, e, nMaquinas, elemento, valores, tiempoEsperado)
                control = Control(maquina, tiempo, e, nMaquinas, elemento, valores, tiempoEsperado)
                ejecucion=control.algoritmo(i)
                i += 1

            id=ejecucion.id
            for pieza in data[0]:
                for i in range(len(pieza['maquinas'])):
                    datosInput= DatosInput(ejecucion=ejecucion, nPiezaEje=pieza['id'],nFase=i, tiempoRequerido=pieza['tiempos'][i],maquinaNecesaria=pieza['maquinas'][i], valor= pieza['valor'],
                                           tiempoEs=pieza['tiempoEsperado'] , index=pieza['index'][i])
                    datosInput.save()

        else:
            id=-2


        print(id)
        resul = {"id": id}
        resul2 = {"id": id,"aa":'we' ,"d": 'das',"w": 'das'}
        serializer = EjecucionSerializer(data=resul)
        if controlFallo==True:
            return JsonResponse(serializer.errors, status=400)
        print(type(id))
        if type(id) == 'int':
            return JsonResponse(resul, status=201)
        """if serializer.is_valid():
            # serializer.save()
            return JsonResponse(resul, status=201)
        if type(id) == 'int':
            return JsonResponse(resul, status=201)"""
        if(id>-1):
            return JsonResponse(resul, status=201)
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

def resultado_list_detail(request, ejecucion):

    if request.method == 'GET':
        resultado= ResultadoGeneral.objects.filter(id=ejecucion)
        serializer = ResultadoGeneralSerializer(resultado, many=True)
        return JsonResponse(serializer.data, safe=False)
def resultadoFinal_list_detail(request, ejecucion):

    if request.method == 'GET':
        resultadoFinal= ResultadoFinal.objects.filter(ejecucion=ejecucion)
        serializer = ResultadoFinalSerializer(resultadoFinal, many=True)
        return JsonResponse(serializer.data, safe=False)

def fase_list_detail(request, ejecucion):

    if request.method == 'GET':
        resultado= Fase.objects.filter(ejecucion=ejecucion)
        serializer = FaseSerializer(resultado, many=True)
        return JsonResponse(serializer.data, safe=False)
def datosInput_list_detail(request, ejecucion):

    if request.method == 'GET':
        resultado= DatosInput.objects.filter(ejecucion=ejecucion)
        serializer = DatosInputSerializer(resultado, many=True)
        return JsonResponse(serializer.data, safe=False)

def pieza_resultado_list_detail(request, ejecucion):

    if request.method == 'GET':
        resultado= PiezaResultado.objects.filter(ejecucion=ejecucion)
        serializer = PiezaResultadoSerializer(resultado, many=True)
        return JsonResponse(serializer.data, safe=False)

