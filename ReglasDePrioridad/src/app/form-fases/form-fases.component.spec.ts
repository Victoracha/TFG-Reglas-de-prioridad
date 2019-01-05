import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FormFasesComponent } from './form-fases.component';

describe('FormFasesComponent', () => {
  let component: FormFasesComponent;
  let fixture: ComponentFixture<FormFasesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FormFasesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FormFasesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
