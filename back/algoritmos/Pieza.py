class Pieza:
    def __init__(self,  maquinas, tiempos, pieza):
        q=0
        self._nPieza=pieza
        self._fases = []
        self._tiempoTotal = 0
        self._asignatiempo = True
        self._libreMaquina=True

        self._Te = 0
        self._Ad = 0
        self._Ret = 0



        for i in range ( len (tiempos)):
            fase=Fase(self._nPieza, tiempos[i], maquinas[i], i)
            self._fases.append(fase)

    def getNpieza(self):
        return self._nPieza

    def getTiempoEsperado(self):
        return self._Te

    def getAdelanto(self):
        return self._Ad

    def getRetroceso(self):
        return self._Ret

    def getFases(self):
        return self._fases

    def setTiempoTotal(self, tiempo):
        self._tiempoTotal = tiempo
        self._asignatiempo=False

    def getTiempoTotal(self):
        return self._tiempoTotal

    def get_modificartiempo(self):
        return self._asignatiempo

    def set_LibreMaquina(self, libre):
        self._libreMaquina=libre

    def get_LibreMaquina(self, libre):
        return self._libreMaquina
class Fase:
    def __init__(self, nPieza, tiempoRequerido, maquinaNecesaria, nFase):
        self._nPieza=nPieza
        self._tiempoRequerido=tiempoRequerido
        self._maquinaNecesaria=maquinaNecesaria
        self._nFase=nFase

        self._tiempoFaseEntrada = 0
        self._tiempoFaseSalida = 0

    def get_nPieza(self):
        return self._nPieza
    def get_tiempoRequerido(self):
        return self._tiempoRequerido
    def get_maquinaNecesaria(self):
        return self._maquinaNecesaria
    def get_nSubpieza(self):
        return self._nFase

    def get_TiempoEntrada(self):
        return self._tiempoFaseEntrada

    def get_TiempoSalida(self):
        return self._tiempoFaseSalida

    def set_TiempoEntrada(self, tiempo):
        self._tiempoFaseEntrada=tiempo

    def set_TiempoSalida(self, tiempo):
        self._tiempoFaseSalida=tiempo