import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HistorialBaseDatosComponent } from './historial-base-datos.component';

describe('HistorialBaseDatosComponent', () => {
  let component: HistorialBaseDatosComponent;
  let fixture: ComponentFixture<HistorialBaseDatosComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HistorialBaseDatosComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HistorialBaseDatosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
