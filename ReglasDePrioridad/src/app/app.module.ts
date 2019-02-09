import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgxLoadingModule , ngxLoadingAnimationTypes } from 'ngx-loading';

import { AppComponent } from './app.component';

import { MenuInputEjecucionComponent } from './menu-input-ejecucion/menu-input-ejecucion.component';
import { AppRoutingModule } from './app-routing.module';
import { HomeComponent } from './home/home.component';
import { InputManualComponent } from './input-manual/input-manual.component';

import { HttpClientModule } from  '@angular/common/http';

import { TablaResultadosComponent } from './tabla-resultados/tabla-resultados.component';
import { HistorialBaseDatosComponent } from './historial-base-datos/historial-base-datos.component';
import { AyudaComponent } from './ayuda/ayuda.component';


@NgModule({
  declarations: [
    AppComponent,
   
    MenuInputEjecucionComponent,
    HomeComponent,
    InputManualComponent,
 
    TablaResultadosComponent,
    HistorialBaseDatosComponent,
    AyudaComponent
    
  ],
  imports: [
    NgxLoadingModule.forRoot({animationType: ngxLoadingAnimationTypes.wanderingCubes,
      backdropBackgroundColour: 'rgba(0,0,0,0.1)', 
      backdropBorderRadius: '4px',
      primaryColour: '#ffffff', 
      secondaryColour: '#ffffff', 
      tertiaryColour: '#ffffff'}),
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }