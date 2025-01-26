import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { TempHumComponent } from './temp-hum/temp-hum.component';
import { ClockComponent } from './clock/clock.component';
import { GalleryComponent } from './gallery/gallery.component';

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    ClockComponent,
    TempHumComponent,
    GalleryComponent,
    // Import TempHumComponent bezpośrednio
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  standalone: true // Dodaj standalone: true do dekoratora komponentu
})
export class AppComponent {
  title = 'raspberry';
}
