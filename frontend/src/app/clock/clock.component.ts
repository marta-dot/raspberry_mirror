import { Component, OnDestroy, OnInit } from '@angular/core';

@Component({
  selector: 'app-clock',
  standalone: true,
  templateUrl: './clock.component.html',
  imports: [],
  styleUrls: ['./clock.component.css']
})
export class ClockComponent implements OnInit, OnDestroy {
  currentTime: string = '';
  private intervalId: any;

  ngOnInit(): void {
    this.reloadTime();
    this.intervalId = setInterval(() => this.reloadTime(), 1000); // aktualizacja co sekundę
  }

  ngOnDestroy(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId); // zatrzymanie timera przy zniszczeniu komponentu
      //zwalnianie zasobów przy nieużywaniu
    }
  }

  private reloadTime(): void {
    const now = new Date();
    this.currentTime = now.toLocaleTimeString(); // format lokalny
  }
}
