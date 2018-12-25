import Maquina
import Pieza


class Executor():
    def __init__(self, piezas,maquinas, nMaquinas, algoritmo, algoritmoAux):
        self._piezas=piezas
        self._maquinas=maquinas
        self._nMaquinas=nMaquinas
        self._algoritmo=algoritmo
        self._algoritmoAux=algoritmoAux
        self._tiempo=0
        self._PiezasEjecutadas=[]
        for Pieza in self._piezas:
            self._PiezasEjecutadas.append(Pieza.getFases())

    def ejecutar(self):
        a=0
        setAct=[]
        candidatosMaquinas=[]
        librePiezasMaquinas=True
        while a==0:
            #for maquina in self._maquinas:
                #if maquina:
                    #for i in range(len(self._PiezasEjecutadas)):
            i=0
            for maquinaLiberar in self._maquinas:
                faseEliminada=maquinaLiberar.esLibre()
                if len(faseEliminada) >0 and self._tiempo>0:
                    self._PiezasEjecutadas[faseEliminada[0].get_nPieza()-1].pop(0)
                    if len(self._PiezasEjecutadas[faseEliminada[0].get_nPieza()-1]) == 0:
                        self._piezas[faseEliminada[0].get_nPieza() - 1].setTiempoTotal(self._tiempo)
                        #.remove(faseEliminada)
            for piezaEvaluar in self._PiezasEjecutadas:
                librePiezasMaquinas = True
                if len(piezaEvaluar)>0:
                    fase=piezaEvaluar[0]
                    nMaquina=fase.get_maquinaNecesaria()
                    maquinaEvlauar= self._maquinas[nMaquina-1]
                    fa=maquinaEvlauar.PiezaEntradaEspera(fase.get_nPieza())

                    for maq in self._maquinas:
                        if maq.PiezaEntradaEspera(fase.get_nPieza())==True:
                            librePiezasMaquinas=False
                            break

                    if librePiezasMaquinas==True:
                        maquinaEvlauar.guardaFaseCandidata(fase)
                        librePiezasMaquinas = False
                        #piezaEvaluar.remove(fase)

                self._piezas[0].set_LibreMaquina(librePiezasMaquinas)
                i+=1

            for maquinaEjecutada in self._maquinas:

                if self._algoritmo=="spt":
                    #maquinaEjecutada.spt(self._tiempo)
                    maquinaEjecutada.ejecutarFase()

                """and piezaACero.get_modificartiempo== True"""
                maquinaEjecutada.SetTiempo()
            """for piezaACero in self._piezas:
                if piezaACero.get_modificartiempo()== True and len(piezaACero.getFases())==0 and piezaACero.get_LibreMaquina(librePiezasMaquinas)==True  :
                    piezaACero.setTiempoTotal(self._tiempo)"""
            self._tiempo += 0.5
            if self._tiempo == 20:
                a = 1

    """def spt(self, candidatos):
        ganador=[]
        ganadorFase = [999, 999]
        for candidato in candidatos:

            candidatoFase = candidato[1]
            if len(ganador)==0:
                ganadorFase=candidatoFase
                ganador = candidato
            elif candidatoFase[1] < ganadorFase[1]:
                    ganador=candidato
                    ganadorFase = candidatoFase
        return ganador"""

    """if faseActual.get_maquinaNecesaria() == maquina.getNmaquina():
                            setAct = [i, faseActual]
                            candidatosMaquinas.append(setAct)
                self._tiempo+=0.5
                if self._tiempo==3:
                    a=1

                i += 1
                if len(candidatosMaquinas) > 1:
                    ganador = self.spt(candidatosMaquinas)

                elif len(candidatosMaquinas) == 1:
                    ganador = candidatosMaquinas[0]
                if len(candidatosMaquinas) > 0:
                    index = ganador[0]

                    elemento = self._PiezasEjecutadas[ganador[0]]
                    del elemento[0]
                    self._PiezasEjecutadas[ganador[0]] = elemento"""