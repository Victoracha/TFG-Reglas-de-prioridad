import Pieza
import Maquina
import Executor
class Control():
    def __init__(self, piezas_maquina, piezas_tiempo, n_maquinas=3):
        self._piezas = []
        #Pieza()
        self._n_maquinas=n_maquinas
        self._maquinas = []

        for i in range (self._n_maquinas):
            self._maquinas.append(Maquina.Maquina(i+1, len(piezas_maquina)))
        for i in range(len(piezas_maquina)):
            self._piezas.append(Pieza.Pieza(piezas_maquina[i], piezas_tiempo[i], i+1))


    def algoritmo (self, algoritmo="spt", algoritmoAux="fifo"):

            ejecucion= Executor.Executor(self._piezas, self._maquinas, self._n_maquinas, algoritmo, algoritmoAux)
            ejecucion.ejecutar()
            #for piezaEvaTiempo
            return 0