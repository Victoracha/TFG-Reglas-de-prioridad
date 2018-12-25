import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MenuInputEjecucionComponent } from './menu-input-ejecucion.component';

describe('MenuInputEjecucionComponent', () => {
  let component: MenuInputEjecucionComponent;
  let fixture: ComponentFixture<MenuInputEjecucionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MenuInputEjecucionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MenuInputEjecucionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
