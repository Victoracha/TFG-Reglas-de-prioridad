import { Component, OnInit } from '@angular/core';
import { APIService } from '../api.service';
class Ejecutar{
  id: [1000, 20000, 300000]
}
@Component({
  selector: 'app-form-fases',
  templateUrl: './form-fases.component.html',
  styleUrls: ['./form-fases.component.css']
})
export class FormFasesComponent implements OnInit {
  
  constructor(private  apiService:  APIService) { }
  
  ngOnInit() {
    
  }
  createEjecucion(){
  var ejecucion={
    id:[1, 2, 3000]
  };
  this.apiService.postDatosEjecucion(ejecucion).subscribe((Response) => {console.log(Response)})
};
  
}
