import { Component, OnInit } from '@angular/core';
import { APIService } from '../api.service';
import {InputDatos} from '../input'
import { dataLoader } from '@amcharts/amcharts4/core';
class Ejecutar{
  id: [1000, 20000, 300000]
}
@Component({
  selector: 'app-form-fases',
  templateUrl: './form-fases.component.html',
  styleUrls: ['./form-fases.component.css']
})
export class FormFasesComponent implements OnInit {
  
  constructor(private  apiService:  APIService) { APIService}
  datosInput: Array<InputDatos> = [];
  dato= new InputDatos();
  
  ngOnInit() {
    
  }
  add(): void {
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
      this.datosInput[0]=dato
      this.datosInput.push(dato);
    }
    console.log(this.datosInput);
    console.log(this.dato.id);
  }
  createEjecucion(){
  var ejecucion={
    id:[1, 2, 3000]
  };
  this.apiService.postDatosEjecucion(ejecucion).subscribe((Response) => {console.log(Response)})
};
  
}
