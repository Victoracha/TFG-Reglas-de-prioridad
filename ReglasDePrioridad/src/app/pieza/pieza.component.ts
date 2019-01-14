import { Component, OnInit } from '@angular/core';
import { Observable } from "rxjs";
import { HttpClient } from "@angular/common/http";

class Pieza {
  id : number;
  nPieza : Date;
}

@Component({
  selector: 'app-pieza',
  templateUrl: './pieza.component.html',
  styleUrls: ['./pieza.component.css']
})
export class PiezaComponent implements OnInit {
  piezas : Observable<Pieza[]>;
  constructor(private httpClient:HttpClient) {
    
    

   }
   isCollapse = true;
  toggleState() {
    let foo = this.isCollapse
    this.isCollapse = foo === false ? true : false;
  }
  ngOnInit() {
    this.piezas = this.httpClient.get<Pieza[]>("localhost:8000/Pieza")
    
  }

}
