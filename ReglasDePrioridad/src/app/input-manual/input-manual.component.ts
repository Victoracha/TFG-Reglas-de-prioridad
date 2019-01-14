import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import {InputDatos} from '../input';

import { APIService } from '../api.service';

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
  constructor(private apiService: APIService) { }

  ngOnInit() {
  }
  add(valor, tiempoesperado): void {
    let dato= new InputDatos();
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
    if (this.valores){
      dato.valor=valor;
    }
    if (this.tiempoEsperado){
      dato.tiempoEsperado=tiempoesperado;
    }
    console.log(valor);
    console.log(this.datosInput);
    console.log(this.dato);
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
  CrearFase(Maquina, Tiempo){
    if(Maquina && Tiempo){
    this.dato.maquinas.push(+Maquina);
    this.dato.tiempos.push(+Tiempo)
    console.log(this.dato)}
  }
  
  createEjecucion(){
    
    this.apiService.postDatosEjecucion(this.datosInput).subscribe((Response) => {console.log(Response)})
  };
}
