from django.urls import path
from Pieza import views

urlpatterns = [
    path('Pieza/', views.pieza_list),
    path('pieza/', views.pieza_list),
    path('ejecucion/', views.ejecucion_list),
]
