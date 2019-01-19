import { Component, OnInit } from '@angular/core';
import { APIService } from '../api.service';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-historial-base-datos',
  templateUrl: './historial-base-datos.component.html',
  styleUrls: ['./historial-base-datos.component.css']
})
export class HistorialBaseDatosComponent implements OnInit {
  private ejecucion: Array<object> = [];
  ejecutar: Number;
  esEjecucion: Boolean;
  constructor(private apiService: APIService, private route: ActivatedRoute) { }

  ngOnInit() {
    this.ejecutar = +this.route.snapshot.paramMap.get('id');
    console.log(this.ejecucion);
    if(this.ejecutar==1){
      this.esEjecucion=true;
    }else{
      this.esEjecucion=false;
    }
    this.getEjecucion();
  }

  public getEjecucion(){

   

    this.apiService.getEjecucion().subscribe((data: Array<object>) => {
      
      this.ejecucion = data;
      console.log(data);
    });
    
  }

}
