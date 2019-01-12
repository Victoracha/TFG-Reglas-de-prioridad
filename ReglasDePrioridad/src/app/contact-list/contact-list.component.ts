import { Component, OnInit } from '@angular/core';

import { APIService } from '../api.service';
@Component({
  selector: 'app-contact-list',
  templateUrl: './contact-list.component.html',
  styleUrls: ['./contact-list.component.css']
})
export class ContactListComponent implements OnInit {

  private pieza: Array<object> = [];
  private ejecucion: Array<object> = [];
  private fase: Array<object> = [];
  constructor(private apiService: APIService) { }

  ngOnInit() {
    this.getContacts();
  }

  public getContacts(){

    this.apiService.getPieza().subscribe((data: Array<object>) => {
      
      this.pieza = data;
      console.log(data);
    });

    this.apiService.getEjecucion().subscribe((data: Array<object>) => {
      
      this.ejecucion = data;
      console.log(data);
    });
    this.apiService.getEjecucionFases().subscribe((data: Array<object>) => {
      
      this.fase = data;
      console.log(data);
    });
  }

}