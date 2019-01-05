from algoritmos.Pieza import Pieza
from algoritmos.Maquina import  Maquina
from algoritmos.Executor import  Executor
from Pieza.models import Ejecucion, PiezaEje, ResultadoGeneral, PiezaResultado
from django.utils import timezone
class Control():
    def __init__(self, piezas_maquina, piezas_tiempo, data,n_maquinas=3):
        self._piezas = []
        #Pieza()
        self._n_maquinas=n_maquinas
        self._maquinas = []

        self._tiempoMax = 0
        self._tiempoMin = 999999
        self._tiempoMedio = 0
        self._SA = 0
        self._SR = 0
        self._NA = 0
        self._NR = 0

        self._data=data
        for i in range (self._n_maquinas):
            self._maquinas.append(Maquina(i+1, len(piezas_maquina)))
        for i in range(len(piezas_maquina)):
            self._piezas.append(Pieza(piezas_maquina[i], piezas_tiempo[i], i+1))


    def algoritmo (self, algoritmo="spt", algoritmoAux="fifo"):

            ejecucio= Executor(self._piezas, self._maquinas, self._n_maquinas, algoritmo, algoritmoAux)
            ejecucio.ejecutar()
            #for piezaEvaTiempo in self._piezas

            for piezaEvaTiempo in self._piezas:
                if piezaEvaTiempo.getTiempoTotal() > self._tiempoMax:
                    self._tiempoMax = piezaEvaTiempo.getTiempoTotal()
                if piezaEvaTiempo.getTiempoTotal() < self._tiempoMax:
                    self._tiempoMin = piezaEvaTiempo.getTiempoTotal()
                self._tiempoMedio += piezaEvaTiempo.getTiempoTotal()
            self._tiempoMedio /= len(self._piezas)

            e = Ejecucion(fecha=timezone.now())
            e.save()
            for da in self._data.values():
                d=0
            for num in da:
                d=0
            p = PiezaResultado(nPieza=self._maquinas[2].getTiempoMaquina(), ejecucion=e, tiempoEsperado = 0 ,tiempoTotal=0, diferenciaAde=0, diferenciaRetra=0)
            p.save()
            resultado = ResultadoGeneral (id=e, tiempoMax =self._tiempoMax, tiempoMin = self._tiempoMin, tiempoMedio =  self._tiempoMedio
                                          , SA =self._SA, SR =  self._SR, NA = self._NA,NR =  self._NR)

            resultado.save()
            return 0
