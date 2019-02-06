from algoritmos.Pieza import Pieza
from algoritmos.Maquina import  Maquina
from algoritmos.Executor import  Executor

from Pieza.models import Ejecucion, PiezaEje, ResultadoFinal, PiezaResultado, Fase
from django.utils import timezone
class Control():
    def __init__(self, piezas_maquina, piezas_tiempo,e, n_maquinas=3, algoritmo="spt",valor=[] , tiempoEsperado=[] ,data=0):
        self._piezas = []
        #Pieza()
        self._n_maquinas=n_maquinas
        self._maquinas = []
        self._e=e
        self._tiempoEsperados=tiempoEsperado
        self._valores = valor
        self._tiempoMax = 0
        self._tiempoMin = 999999
        self._tiempoMedio = 0
        self._SA = 0
        self._SR = 0
        self._nRetrasos=0
        self._nAdelantos=0
        self._NA= 0
        self._NR= 0
        self._data=data
        self._algoritmo=algoritmo
        for i in range (self._n_maquinas):
            self._maquinas.append(Maquina(i+1, len(piezas_maquina), algoritmo))
        for i in range(len(piezas_maquina)):
            self._piezas.append(Pieza(piezas_maquina[i], piezas_tiempo[i], i+1, self._valores[i], self._tiempoEsperados[i]))
        self._nPiezas=len(self._piezas)

    def algoritmo (self, indiceResultado):
            algoritmo = "spt"
            algoritmoAux = "fifo"
            ejecucio= Executor(self._piezas, self._maquinas, self._n_maquinas, algoritmo, algoritmoAux)
            ejecucio.ejecutar()
            #for piezaEvaTiempo in self._piezas

            for piezaEvaTiempo in self._piezas:
                if piezaEvaTiempo.getTiempoTotal() > self._tiempoMax:
                    self._tiempoMax = piezaEvaTiempo.getTiempoTotal()
                if piezaEvaTiempo.getTiempoTotal() < self._tiempoMax:
                    self._tiempoMin = piezaEvaTiempo.getTiempoTotal()


                if piezaEvaTiempo.getTiempoTotal() <  piezaEvaTiempo.getTiempoEsperado():
                    self._NA += 1
                    self._nAdelantos += 1
                    piezaEvaTiempo.setAdelanto( piezaEvaTiempo.getTiempoEsperado() - piezaEvaTiempo.getTiempoTotal())
                    self._SA+= piezaEvaTiempo.getTiempoEsperado() - piezaEvaTiempo.getTiempoTotal()


                elif piezaEvaTiempo.getTiempoTotal() > piezaEvaTiempo.getTiempoEsperado():
                    self._NR += 1
                    self._nRetrasos += 1
                    piezaEvaTiempo.setRetroceso(piezaEvaTiempo.getTiempoTotal()- piezaEvaTiempo.getTiempoEsperado())
                    self._SR+=piezaEvaTiempo.getTiempoTotal()- piezaEvaTiempo.getTiempoEsperado()
                self._tiempoMedio += piezaEvaTiempo.getTiempoTotal()
            if self._nAdelantos >0:
                self._SA /=self._nAdelantos
            if self._nRetrasos > 0:
                self._SR /=self._nRetrasos
            self._tiempoMedio /= len(self._piezas)

            id=self.guardaPiezas(self._e, indiceResultado)

            return id

    def guardaPiezas(self, e, indiceResultado):
        print("llega")

        print(e)
        if self._algoritmo == "spt":
            self._algoritmo="SPT"
        elif self._algoritmo == "llp":
            self._algoritmo = "LPT"
        elif self._algoritmo == "fifo":
            self._algoritmo = "FIFO"
        elif self._algoritmo == "mayortiempo":
            self._algoritmo = "Mayor Tiempo Restante"
        elif self._algoritmo == "aleatorio":
            self._algoritmo = "Aleatorio"
        elif self._algoritmo == "mayorvalor":
            self._algoritmo = "Mayor Valor de O.F"
        elif self._algoritmo == "edd":
            self._algoritmo = "EDD"
        elif self._algoritmo == "winq":
            self._algoritmo = "WINQ"

        for pieza in self._piezas:
            p = PiezaResultado(nPieza=pieza.getNpieza(), ejecucion=e, tiempoEsperado=pieza.getTiempoEsperado(),
                               tiempoTotal=pieza.getTiempoTotal(),
                               diferenciaAde=pieza.getAdelanto(), diferenciaRetra=pieza.getRetroceso(), indiceResultado=indiceResultado, algoritmo=self._algoritmo)

            p.save()
        resultado = ResultadoFinal( tiempoMax=self._tiempoMax, tiempoMin=self._tiempoMin,
                                     tiempoMedio=self._tiempoMedio
                                     , SA=self._SA, SR=self._SR, NA=self._NA, NR=self._NR, ejecucion=e, algoritmo=self._algoritmo )
        resultado.save()

        for maquina in self._maquinas:
            for faseResul in maquina.getFases():
                if faseResul != 0:
                    coe=faseResul.get_nPieza()*10
                    fase = Fase( nPieza= p, nPiezaEje=faseResul.get_nPieza(), ejecucion=e, nFase=faseResul.get_nSubpieza(), tiempoRequerido = faseResul.get_tiempoRequerido(),
                        maquinaNecesaria= faseResul.get_maquinaNecesaria(), tiempoFaseEntrada= faseResul.get_tiempoFaseEntrada(), tiempoFaseSalida= faseResul.get_tiempoFaseSalida()
                                 , color=coe, brightness=faseResul.get_nPieza()/10, indiceResultado=indiceResultado)

                    fase.save()
        return e
