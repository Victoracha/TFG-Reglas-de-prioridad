import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { MenuInputEjecucionComponent } from './menu-input-ejecucion/menu-input-ejecucion.component'
import { InputManualComponent } from './input-manual/input-manual.component'
import { HomeComponent } from './home/home.component'
import { ContactListComponent } from './contact-list/contact-list.component';
const routes: Routes = [
  { path: 'input', component: MenuInputEjecucionComponent },
  { path: 'input-manual', component: InputManualComponent },
  {
    path:  'contacts',
    component:  ContactListComponent
  },
  { path: 'home', component: HomeComponent }
  //{ path: '', redirectTo: '/dashboard', pathMatch: 'full' }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }