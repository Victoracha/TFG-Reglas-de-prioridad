import { Component, OnInit } from '@angular/core';
import { APIService } from '../api.service';
@Component({
  selector: 'app-tabla-resultados',
  templateUrl: './tabla-resultados.component.html',
  styleUrls: ['./tabla-resultados.component.css']
})
export class TablaResultadosComponent implements OnInit {
  private resultado: Array<object> = [];
  private resultadoPiezas: Array<object> = [];
  constructor(private apiService: APIService) { }

  ngOnInit() {
    this.getResultados()
    
  }
  getResultados(){
    
    this.apiService.getPiezaResultado().subscribe((data: Array<object>) => {
      
      this.resultadoPiezas = data;
      console.log(data);
    });
  this.apiService.getTablaResultados().subscribe((data: Array<object>) => {
      
    this.resultado = [data];
    console.log(data);
  });
}
}
