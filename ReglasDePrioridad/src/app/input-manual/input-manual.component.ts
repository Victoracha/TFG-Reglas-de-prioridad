import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import {InputDatos} from '../input';

import { APIService } from '../api.service';
import { PiezaComponent } from '../pieza/pieza.component';

@Component({
  selector: 'app-input-manual',
  templateUrl: './input-manual.component.html',
  styleUrls: ['./input-manual.component.css']
})
export class InputManualComponent implements OnInit {

  datosInput: Array<InputDatos> = [];
  dato= new InputDatos();
  private estado=true;
  element = <HTMLInputElement> document.getElementById("is3dCheckBox");
  private valores=true;
  private tiempoEsperado=true;
  private maquinetemp=0;
  private tiempotemp=0;
  constructor(private apiService: APIService) { }

  ngOnInit() {
  }
  add(valor, tiempoesperado): void {
    let dato= new InputDatos();
    if (this.valores){
      dato.valor=0;
    }
    if (this.tiempoEsperado){
      dato.tiempoEsperado=0;
    }
    console.log(valor);
    console.log(this.datosInput);
    console.log(this.dato);
    if ( this.datosInput.length == 0)
    {
      dato.id = 1;
      
      dato.maquinas=[];
      dato.tiempos=[];
      this.datosInput.push(dato);
    }else{
      dato.id = this.datosInput[this.datosInput.length-1].id +1;
      dato.maquinas=[];
      dato.tiempos=[];
      
      //this.datosInput[0]=dato
      this.datosInput.push(dato);
    }
    
  }

  eliminaOT(index){
    
    this.datosInput.splice(index.id-1,1);
    
    for (var _i = index.id-1; _i < this.datosInput.length; _i++) {
      console.log(this.datosInput[_i]);
      this.datosInput[_i].id=_i+1;
    }
    console.log(this.datosInput);
  }

  envia(ot): void {
    this.estado=false;
    this.dato=ot;
  }
  cancelar(id):void{

    /*this.estado=true;
    this.datosInput[id].tiempos=[];
    this.datosInput[id].maquinas=[];
    console.log(this.datosInput);*/
  }
  guardar(id):void{
    console.log(id);
    console.log(this.dato);
    this.estado=true;
    this.datosInput[id-1]=this.dato;

    console.log(this.datosInput);
  }
  guardarValor(valor){
    if (this.valores){
      this.dato.valor=valor;
    }
  
  }
  guardarTiempoEsperado(tiempo){
    if (this.tiempoEsperado){
      this.dato.tiempoEsperado=tiempo;
    }
    
  }
  
    
    
  CrearFase(Maquina, Tiempo){
    if(Maquina && Tiempo){
      
      this.dato.maquinas.push(+Maquina);
      this.dato.tiempos.push(+Tiempo)
      console.log(this.dato);
      if ( this.dato.index.length == 0){
        this.dato.index.push(0)
      }else{
        this.dato.index.push( +this.dato.index[this.dato.index.length-1] +1)
      }
  }
  }

  ActualizarFase(Maquina, Tiempo, index){
    console.log(index)
    this.dato.maquinas[index]=this.maquinetemp;
    this.dato.tiempos[index]=+Tiempo;
    console.log(this.dato);
    console.log(this.maquinetemp);
    console.log(index)
  }
  actualizaMaquina(maquina){
    this.maquinetemp=+maquina;
    
  }
  EliminarFase(Maquina, Tiempo,index){
    console.log(this.dato)
    console.log(index)
    this.dato.maquinas.splice(index,1);
    
    this.dato.tiempos.splice(index,1);
    this.dato.index.splice(-1,1);
    console.log(this.dato);
  }
  
  createEjecucion(){
    
    this.apiService.postDatosEjecucion(this.datosInput).subscribe((Response) => {console.log(Response)})
  };
}
