import { Injectable } from  '@angular/core';
import {HttpHeaders, HttpClient} from  '@angular/common/http';
import { catchError, tap } from 'rxjs/operators';
import { Observable, of } from 'rxjs';
import {InputDatos} from './input';
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

  getPiezaResultado(idEjecucion: number){
      
    return  this.httpClient.get(`${this.API_URL}/pieza/`+ idEjecucion);
}

  getEjecucion(){
      
    return  this.httpClient.get(`${this.API_URL}/ejecucion/`);
}

getTablaResultados(idEjecucion: number){
      
    return  this.httpClient.get(`${this.API_URL}/resultado/`+ idEjecucion);
}

getEjecucionFases(idEjecucion: number){
    return  this.httpClient.get(`${this.API_URL}/fase/`+ idEjecucion);
}

getDatosInput(idEjecucion: number){
    return  this.httpClient.get(`${this.API_URL}/datosInput/`+ idEjecucion);
}
postDatosEjecucion(fases){
      return this.httpClient.post(`${this.API_URL}/ejecucion/`, fases);
  }
  enviaEjecucion(id: number){
      return id;
  }
  
}