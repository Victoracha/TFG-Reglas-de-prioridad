from algoritmosTFG import Pieza
from algoritmosTFG import Maquina
from algoritmosTFG import Executor
from planificador.models import PiezaEjecucion
from planificador.models import FaseEjecucion
from planificador.models import MaquinaEjecucion
from planificador.models import Maquinas_Ejecutadas
class Control():
    def __init__(self, piezas_maquina, piezas_tiempo, n_maquinas=3):
        self._piezas = []
        #Pieza()
        self._n_maquinas=n_maquinas
        self._maquinas = []

        for i in range (self._n_maquinas):
            self._maquinas.append(Maquina.Maquina(i+1, len(piezas_maquina)))
        for i in range(len(piezas_maquina)):
            self._piezas.append(Pieza(piezas_maquina[i], piezas_tiempo[i], i + 1))


    def algoritmo (self, algoritmo="spt", algoritmoAux="fifo"):

            ejecucion= Executor.Executor(self._piezas, self._maquinas, self._n_maquinas, algoritmo, algoritmoAux)
            ejecucion.ejecutar()
            #for piezaEvaTiempo
            """for pieza in Pieza:
                pieza_record=PiezaEjecucion(nPieza=pieza.getFases()[0].get_nPieza())
                pieza_record.save()"""
            return 0