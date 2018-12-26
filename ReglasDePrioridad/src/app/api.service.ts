import { Injectable } from  '@angular/core';
import {HttpHeaders, HttpClient} from  '@angular/common/http';
import { catchError, tap } from 'rxjs/operators';
import { Observable, of } from 'rxjs';
@Injectable({
providedIn:  'root'
})

export  class  APIService {
  API_URL  =  'http://localhost:8000';
  constructor(private  httpClient:  HttpClient) {}
  getPieza(){
      
      return  this.httpClient.get(`${this.API_URL}/Pieza/`);
  }
  getEjecucion(){
      
    return  this.httpClient.get(`${this.API_URL}/ejecucion/`);
}
}