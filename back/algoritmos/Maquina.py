import random
class Maquina:
    def __init__(self, nMaquina, nPiezas):
        self._ejecucion = []
        self._nMaquina=nMaquina

        self._libre=True

        self._tiempoEjecucionFase=0
        self._tiempoActual = 0

        self._candidatos=[]

        self._faseActualMaquina=[]

        self._FasesEjecutadasLista=[]
        self._FasesEjecutadasHisto=[]

        self._piezasEspera = {}
        for i in range(nPiezas):
            self._piezasEspera[i+1]=False
    def getFases(self):
        return  self._FasesEjecutadasHisto
    def getEjecucion(self):
        return self._ejecucion
    def getNmaquina(self):
        return self._nMaquina
    def getTiempoMaquina(self):
        return self._tiempoActual
    def setEjecucion(self, nPieza):
        if nPieza != 0:
            self._ejecucion.append(nPieza)
        else:
            self._ejecucion.append(0)

    def esLibre(self):
        faseEliminada=self._faseActualMaquina
        if len(self._faseActualMaquina) > 0:
            if self._libre==False:
                diferenciaTiempo = self._tiempoActual - self._tiempoEjecucionFase
                if diferenciaTiempo==self._faseActualMaquina[0].get_tiempoRequerido():
                    self._piezasEspera[self._faseActualMaquina[0].get_nPieza()]=False
                    self._libre=True
                    if self._faseActualMaquina[0] in self._candidatos:
                        self._FasesEjecutadasHisto[-1].set_TiempoSalida(self._tiempoActual)
                        self._candidatos.remove(self._faseActualMaquina[0])
                        self._faseActualMaquina=[]
                        return faseEliminada
        return []
                        #self._tiempoEjecucionFase=self._tiempoActual
    def guardaFaseCandidata(self, fase):
        self._candidatos.append(fase)
        self._piezasEspera[fase.get_nPieza()]=True
    """def resetTiempoEjecucionProceso(self):
        self._tiempoEjecucionProceso = 0"""

    def PiezaEntradaEspera(self, nPieza):
        return self._piezasEspera[nPieza]
    def SetTiempo(self):
        self._tiempoActual+=0.5
        if len(self._faseActualMaquina) > 0:
            self._FasesEjecutadasHisto.append(self._faseActualMaquina[0])
        else:
            self._FasesEjecutadasHisto.append(0)
    def ejecutarFase(self):
        #self.esLibre()
        if len(self._candidatos) >0 and self._libre==True:
            #self.spt()
            #self.fifo()
            #self.llp()
            self.mayorTiempoOperacionesRestantes()
            self._libre =False
            if len(self._faseActualMaquina) > 0:
                self._FasesEjecutadasLista.append(self._faseActualMaquina[0])
    def spt(self):


        for candidato in self._candidatos:


            if len(self._faseActualMaquina) == 0:
                self._faseActualMaquina=[candidato]
                self._tiempoEjecucionFase = self._tiempoActual
                candidato.set_TiempoEntrada(self._tiempoActual)
            elif self._faseActualMaquina[0].get_tiempoRequerido() > candidato.get_tiempoRequerido():
                self._faseActualMaquina = [candidato]
                self._tiempoEjecucionFase = self._tiempoActual
                candidato.set_TiempoEntrada(self._tiempoActual)

    def llp(self):
        for candidato in self._candidatos:


            if len(self._faseActualMaquina) == 0:
                self._faseActualMaquina=[candidato]
                self._tiempoEjecucionFase = self._tiempoActual
                candidato.set_TiempoEntrada(self._tiempoActual)
            elif self._faseActualMaquina[0].get_tiempoRequerido() < candidato.get_tiempoRequerido():
                self._faseActualMaquina = [candidato]
                self._tiempoEjecucionFase = self._tiempoActual
                candidato.set_TiempoEntrada(self._tiempoActual)

    def mayorTiempoOperacionesRestantes(self):
        for candidato in self._candidatos:

            if len(self._faseActualMaquina) == 0:
                self._faseActualMaquina = [candidato]
                self._tiempoEjecucionFase = self._tiempoActual
                candidato.set_TiempoEntrada(self._tiempoActual)
            elif self._faseActualMaquina[0].get_tiempoOperacionalRestante() < candidato.get_tiempoOperacionalRestante():
                self._faseActualMaquina = [candidato]
                self._tiempoEjecucionFase = self._tiempoActual
                candidato.set_TiempoEntrada(self._tiempoActual)
    def fifo(self):
        self._faseActualMaquina = [self._candidatos[0]]
        self._tiempoEjecucionFase = self._tiempoActual
        self._candidatos[0].set_TiempoEntrada(self._tiempoActual)

    def aleatorio(self):
        self._faseActualMaquina = [random.choice(self._candidatos[0])]
        self._tiempoEjecucionFase = self._tiempoActual
        self._faseActualMaquina.set_TiempoEntrada(self._tiempoActual)

