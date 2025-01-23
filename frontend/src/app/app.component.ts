import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { TempHumComponent } from './temp-hum/temp-hum.component';
import { ClockComponent } from './clock/clock.component';

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    ClockComponent,
    TempHumComponent // Import TempHumComponent bezpośrednio
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  standalone: true // Dodaj standalone: true do dekoratora komponentu
})
export class AppComponent {
  title = 'raspberry';
}
