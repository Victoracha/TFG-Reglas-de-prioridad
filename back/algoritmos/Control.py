from algoritmos.Pieza import Pieza
from algoritmos.Maquina import  Maquina
from algoritmos.Executor import  Executor
from Pieza.models import Ejecucion, PiezaEje, ResultadoGeneral, PiezaResultado, Fase
from django.utils import timezone
class Control():
    def __init__(self, piezas_maquina, piezas_tiempo, data=0,n_maquinas=3):
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


            """for da in self._data.values():
                d=0
            for num in da:
                d=0"""

            id=self.guardaPiezas()

            return id

    def guardaPiezas(self):

        e = Ejecucion(fecha=timezone.now())
        e.save()
        for pieza in self._piezas:
            p = PiezaResultado(nPieza=pieza.getNpieza(), ejecucion=e, tiempoEsperado=pieza.getTiempoEsperado(),
                               tiempoTotal=pieza.getTiempoTotal(),
                               diferenciaAde=pieza.getAdelanto(), diferenciaRetra=pieza.getRetroceso())

            p.save()
        resultado = ResultadoGeneral(id=e, tiempoMax=self._tiempoMax, tiempoMin=self._tiempoMin,
                                     tiempoMedio=self._tiempoMedio
                                     , SA=self._SA, SR=self._SR, NA=self._NA, NR=self._NR)
        resultado.save()

        for maquina in self._maquinas:
            for faseResul in maquina.getFases():
                if faseResul != 0:
                    coe=faseResul.get_nPieza()*10
                    fase = Fase( nPieza= p, nPiezaEje=faseResul.get_nPieza(), ejecucion=e, nFase=faseResul.get_nSubpieza(), tiempoRequerido = faseResul.get_tiempoRequerido(),
                        maquinaNecesaria= faseResul.get_maquinaNecesaria(), tiempoFaseEntrada= faseResul.get_tiempoFaseEntrada(), tiempoFaseSalida= faseResul.get_tiempoFaseSalida()
                                 , color=coe, brightness=faseResul.get_nPieza()/10)

                    fase.save()
        return e.id
