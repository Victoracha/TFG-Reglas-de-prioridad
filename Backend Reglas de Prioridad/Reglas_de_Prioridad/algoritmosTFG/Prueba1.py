import Control
from django.core.exceptions import ImproperlyConfigured
piezas_maquina=[[2,3,1],[2,1,2,3],[3,1,2], [2,3,1,2],[3,2]]
piezas_tiempo=[[2,2,1],[0.5,2,0.5,2.5],[1.5,2.5,1], [1,2.5,3,1],[0.5,2]]

control= Control.Control(piezas_maquina, piezas_tiempo)
control.algoritmo()
a=2