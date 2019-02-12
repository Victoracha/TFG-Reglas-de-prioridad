import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { InputDatos } from '../input';
import { NgxLoadingModule, ngxLoadingAnimationTypes } from 'ngx-loading';
import { APIService } from '../api.service';

import { DataSource } from '@amcharts/amcharts4/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-input-manual',
  templateUrl: './input-manual.component.html',
  styleUrls: ['./input-manual.component.css']
})
export class InputManualComponent implements OnInit, NgxLoadingModule {

  datosInput: Array<InputDatos> = [];
  dato = new InputDatos();
  estado = true;
  element = <HTMLInputElement>document.getElementById("is3dCheckBox");
  valores = true;
  tiempoEsperado = true;
  verEjecucion = false;
  maquinetemp = 0;
  tiempotemp = 0;
  haCambiadoMaq = false;
  haCambiadoTem = false;
  getEjecucion = true;
  idEjecucionAtras = 0;
  loading = false;
  controlEjecucion = false;
  errorPost = false;

  isSpt = false;
  isLpt = false;
  isFifo = false;
  isAlea = false;
  isMaValor = false;
  isEdd = false;
  isWinq = false;
  isTiempoRes = false;
  algoritmos = [];
  nPiezas = [];
  datoCargaIds = [];
  contaExtraeNPieza = 0;
  idEje: number = 2;
  constructor(private apiService: APIService, private route: ActivatedRoute) { }

  ngOnInit() {
    this.idEjecucionAtras = +this.route.snapshot.paramMap.get('id');
    if (this.idEjecucionAtras > 0)
      this.inicializaDatos(this.idEjecucionAtras);


  }
  inicializaDatos(idEje) {
    this.apiService.getDatosInput(idEje).subscribe((data: Array<object>) => {
      console.log(data);
      for (var elemento of data) {
        let dato = new InputDatos();
        if (this.datoCargaIds.includes(elemento['nPiezaEje'])) {
          this.datosInput[elemento['nPiezaEje'] - 1].maquinas.push(elemento['maquinaNecesaria']);
          this.datosInput[elemento['nPiezaEje'] - 1].tiempos.push(elemento['tiempoRequerido']);
          this.datosInput[elemento['nPiezaEje'] - 1].index.push(elemento['index']);
          this.controlEjecucion = true;

        } else {
          this.datoCargaIds.push(elemento['nPiezaEje']);
          console.log(this.datoCargaIds);
          dato.id = elemento['nPiezaEje'];
          dato.valor = elemento['valor'];
          dato.tiempoEsperado = elemento['tiempoEs'];

          dato.maquinas.push(elemento['maquinaNecesaria']);
          dato.tiempos.push(elemento['tiempoRequerido']);
          dato.index.push(elemento['index']);
          this.datosInput.push(dato);

        }
        this.contaExtraeNPieza += 1;
        this.nPiezas.push(this.contaExtraeNPieza);
        console.log(this.datoCargaIds);


      }

      console.log(this.dato);
      console.log(this.datosInput);
    });


  }
  add(valor, tiempoesperado): void {
    let dato = new InputDatos();
    if (this.valores) {
      dato.valor = 0;
    }
    if (this.tiempoEsperado) {
      dato.tiempoEsperado = 0;
    }
    console.log(valor);
    console.log(this.datosInput);
    console.log(this.dato);
    if (this.datosInput.length == 0) {
      dato.id = 1;

      dato.maquinas = [];
      dato.tiempos = [];
      this.controlEjecucion = true;
      this.datosInput.push(dato);
    } else {
      dato.id = this.datosInput[this.datosInput.length - 1].id + 1;
      dato.maquinas = [];
      dato.tiempos = [];
      this.datosInput.push(dato);
    }
    this.nPiezas.push(dato.id);
    console.log(this.nPiezas)
  }

  eliminaOT(index) {
    console.log(index)
    this.nPiezas.splice(index - 1, 1);
    this.datosInput.splice(index.id - 1, 1);
    console.log(this.nPiezas)
    let i = 1;
    for (let dato of this.datosInput) {
      dato.id = i;
      i++;
    }
    console.log(this.datosInput);

  }
  envia(ot): void {
    this.estado = false;
    this.dato = ot;
  }
  cancelar(id): void {
  }
  guardar(id): void {
    console.log(id);
    console.log(this.dato);
    this.estado = true;
    this.datosInput[id - 1] = this.dato;

    console.log(this.datosInput);
  }
  guardarValor(valor) {
    if (this.valores) {
      this.dato.valor = +valor;
    }

  }
  guardarTiempoEsperado(tiempo) {
    if (this.tiempoEsperado) {
      this.dato.tiempoEsperado = +tiempo;
    }

  }



  CrearFase(Maquina, Tiempo) {
    if (Maquina && Tiempo) {

      this.dato.maquinas.push(+Maquina);
      this.dato.tiempos.push(+Tiempo)
      console.log(this.dato);
      if (this.dato.index.length == 0) {
        this.dato.index.push(0)
      } else {
        this.dato.index.push(+this.dato.index[this.dato.index.length - 1] + 1)
      }
    }
  }

  ActualizarFase(Maquina, Tiempo, index) {
    console.log(index)
    if (this.haCambiadoMaq)
      this.dato.maquinas[index] = +this.maquinetemp;
    if (this.haCambiadoTem)
      this.dato.tiempos[index] = +this.tiempotemp;
    console.log(this.dato);
    console.log(this.maquinetemp);
    console.log(index)
  }
  actualizaMaquina(maquina) {
    this.maquinetemp = +maquina;
    this.haCambiadoMaq = true;
  }

  actualizaTiempo(tiempo) {
    this.tiempotemp = +tiempo;
    this.haCambiadoTem = true;
  }

  EliminarFase(index) {
    console.log(this.dato)
    console.log(index)
    this.dato.maquinas.splice(index, 1);

    this.dato.tiempos.splice(index, 1);
    this.dato.index.splice(-1, 1);
    console.log(this.dato);
  }
  spt() {
    if (!this.isSpt) {
      this.isSpt = true;
      this.algoritmos.push("spt");
      console.log(this.algoritmos);
    } else {
      this.isSpt = false;
      this.algoritmos.splice(this.algoritmos.indexOf("spt"), 1);
      console.log(this.algoritmos);
    }
    console.log(this.isSpt)
  }

  lpt() {
    if (!this.isLpt) {
      this.isLpt = true;
      this.algoritmos.push("llp");
      console.log(this.algoritmos);
    } else {
      this.isLpt = false;
      this.algoritmos.splice(this.algoritmos.indexOf("llp"), 1);
      console.log(this.algoritmos);
    }
    console.log(this.isLpt)
  }

  fifo() {
    if (!this.isFifo) {
      this.isFifo = true;
      this.algoritmos.push("fifo");
      console.log(this.algoritmos);
    } else {
      this.isFifo = false;
      this.algoritmos.splice(this.algoritmos.indexOf("fifo"), 1);
      console.log(this.algoritmos);
    }
    console.log(this.isFifo)
  }
  aleatorio() {
    if (!this.isAlea) {
      this.isAlea = true;
      this.algoritmos.push("aleatorio");
      console.log(this.algoritmos);
    } else {
      this.isAlea = false;
      console.log(this.algoritmos.indexOf("aleatorio"))
      this.algoritmos.splice(this.algoritmos.indexOf("aleatorio"), 1);

      console.log(this.algoritmos);
    }
    console.log(this.isAlea)
  }

  mayorValor() {
    if (!this.isMaValor) {
      this.isMaValor = true;
      this.algoritmos.push("mayorvalor");
      console.log(this.algoritmos);
    } else {
      this.isMaValor = false;
      this.algoritmos.splice(this.algoritmos.indexOf("mayorvalor"), 1);
      console.log(this.algoritmos);
    }
    console.log(this.isMaValor)
  }

  edd() {
    if (!this.isEdd) {
      this.isEdd = true;
      this.algoritmos.push("edd");
      console.log(this.algoritmos);
    } else {
      this.isEdd = false;
      this.algoritmos.splice(this.algoritmos.indexOf("edd"), 1);
      console.log(this.algoritmos);
    }
    console.log(this.isEdd)
  }



  createEjecucion() {
    this.errorPost = false;
    this.loading = true;
    var consigueLlamada = false;
    var id = this.apiService.postDatosEjecucion([this.datosInput, this.algoritmos]).subscribe((Response) => {
      consigueLlamada = true; console.log(Response); this.idEje = +Response['id'];
      console.log(Response['id']);
      var tipo = typeof Response['id'];
      if (tipo == "number") {
        this.verEjecucion = true;
        this.loading = false;
      }



      console.log(this.idEje);
    },
      (error) => {
        this.loading = false;
        this.errorPost = true;
      }
    )



  };

  wWinq() {
    if (!this.isWinq) {
      this.isWinq = true;
      this.algoritmos.push("winq");
      console.log(this.algoritmos);
    } else {
      this.isWinq = false;
      this.algoritmos.splice(this.algoritmos.indexOf("winq"), 1);
      console.log(this.algoritmos);
    }
    console.log(this.isWinq)
  }

  mayorTiempo() {
    if (!this.isTiempoRes) {
      this.isTiempoRes = true;
      this.algoritmos.push("mayortiempo");
      console.log(this.algoritmos);
    } else {
      this.isTiempoRes = false;
      this.algoritmos.splice(this.algoritmos.indexOf("mayortiempo"), 1);
      console.log(this.algoritmos);
    }
    console.log(this.isTiempoRes)
  }
  Selccionartodos() {
    this.isAlea = true;
    this.isEdd = true;
    this.isWinq = true;
    this.isFifo = true;
    this.isMaValor = true;
    this.isSpt = true;
    this.isLpt = true;
    this.isTiempoRes = true;
    this.algoritmos.push("spt");
    this.algoritmos.push("llp");
    this.algoritmos.push("fifo");
    this.algoritmos.push("aleatorio");
    this.algoritmos.push("mayorvalor");
    this.algoritmos.push("edd");
    this.algoritmos.push("mayortiempo");
    this.algoritmos.push("winq");
  }
  DeSelccionartodos() {
    this.isAlea = false;
    this.isEdd = false;
    this.isWinq = false;
    this.isFifo = false;
    this.isMaValor = false;
    this.isSpt = false;
    this.isLpt = false;
    this.isTiempoRes = false;
    this.algoritmos=[];
  }

}
