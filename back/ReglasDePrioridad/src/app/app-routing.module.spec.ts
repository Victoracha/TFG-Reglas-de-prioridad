import { AppRoutingModule } from './app-routing.module';
import { APIService } from './api.service';
import { TestBed, inject } from '@angular/core/testing';
describe('APIService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [APIService]
    });
  });

  it('should be created', inject([APIService], (service: APIService) => {
    expect(service).toBeTruthy();
  }));
});