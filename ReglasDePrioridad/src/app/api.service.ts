import { Injectable } from  '@angular/core';
import {HttpHeaders, HttpClient} from  '@angular/common/http';
import { catchError, tap } from 'rxjs/operators';
import { Observable, of } from 'rxjs';
const httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

@Injectable({
providedIn:  'root'
})

export  class  APIService {
  API_URL  =  'http://localhost:8000';
  constructor(private  httpClient:  HttpClient) {}
  getPieza(){
      
      return  this.httpClient.get(`${this.API_URL}/Pieza/`);
  }

  getPiezaResultado(){
      
    return  this.httpClient.get(`${this.API_URL}/pieza/48`);
}

  getEjecucion(){
      
    return  this.httpClient.get(`${this.API_URL}/ejecucion/`);
}

getTablaResultados(){
      
    return  this.httpClient.get(`${this.API_URL}/resultado/42/`);
}

getEjecucionFases(){
    return  this.httpClient.get(`${this.API_URL}/fase/53/`);
}
  postDatosEjecucion(fases){
      return this.httpClient.post(`${this.API_URL}/ejecucion/`, fases);
  }
}