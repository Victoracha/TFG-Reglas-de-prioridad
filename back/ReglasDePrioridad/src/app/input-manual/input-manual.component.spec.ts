import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InputManualComponent } from './input-manual.component';

describe('InputManualComponent', () => {
  let component: InputManualComponent;
  let fixture: ComponentFixture<InputManualComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InputManualComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InputManualComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
