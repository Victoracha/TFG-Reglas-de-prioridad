from django.urls import path
from Pieza import views

urlpatterns = [
    path('Pieza/', views.pieza_list),
    path('pieza/<int:ejecucion>/', views.pieza_resultado_list_detail),
    path('fase/<int:ejecucion>/', views.fase_list_detail),
    path('datosInput/<int:ejecucion>/', views.datosInput_list_detail),
    path('ejecucion/', views.ejecucion_list),
    path('resultado/', views.resultado_list),
    path('resultadofinal/<int:ejecucion>/', views.resultadoFinal_list_detail)
]
