from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Pieza.models import Pieza
from Pieza.serializers import PiezaSerializer

@csrf_exempt
def pieza_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    """try:
        piezas = Pieza.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    pk=str(pk)"""
    if request.method == 'GET':
        piezas= Pieza.objects.all()
        serializer = PiezaSerializer(piezas, many=True)
        return JsonResponse(serializer.data, safe=False)
