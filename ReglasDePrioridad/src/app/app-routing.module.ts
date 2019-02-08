import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { MenuInputEjecucionComponent } from './menu-input-ejecucion/menu-input-ejecucion.component';
import { InputManualComponent } from './input-manual/input-manual.component'
import { HomeComponent } from './home/home.component'
import { ContactListComponent } from './contact-list/contact-list.component';
import { PiezaComponent } from './pieza/pieza.component';
import { FormFasesComponent } from './form-fases/form-fases.component';
import { TablaResultadosComponent } from './tabla-resultados/tabla-resultados.component';
import { HistorialBaseDatosComponent } from './historial-base-datos/historial-base-datos.component';
import { AyudaComponent } from './ayuda/ayuda.component';

const routes: Routes = [
  { path: 'input', component: MenuInputEjecucionComponent },
  { path: 'historial/:id', component: HistorialBaseDatosComponent },
  { path: 'input-manual/:id', component: InputManualComponent },
  
  {
    path:  'contacts',
    component:  ContactListComponent
  },
  {
    path:  'pieza',
    component: PiezaComponent
  },
  { path: 'home', component: HomeComponent },
  { path: 'ayuda', component: AyudaComponent },
  { path: 'form-fases', component: FormFasesComponent },
  { path: 'tabla-resultados', component: TablaResultadosComponent },
  { path: 'tabla-resultados/:id', component: TablaResultadosComponent }
  //{ path: '', redirectTo: '/dashboard', pathMatch: 'full' }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }