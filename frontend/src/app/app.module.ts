import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ClockComponent } from './clock/clock.component';
import { TempHumComponent } from './temp-hum/temp-hum.component';

@NgModule({
  imports: [
    BrowserModule,
    ClockComponent,
    TempHumComponent
  ],
  providers: []
})
export class AppModule { }
