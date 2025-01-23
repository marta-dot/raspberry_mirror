import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TempHumComponent } from './temp-hum.component';

describe('TempHumComponent', () => {
  let component: TempHumComponent;
  let fixture: ComponentFixture<TempHumComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TempHumComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TempHumComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
