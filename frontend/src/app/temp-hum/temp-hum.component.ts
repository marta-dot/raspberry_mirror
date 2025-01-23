// temp-hum.component.ts
import { Component, OnInit } from '@angular/core';
import { TempHumService } from './temp-hum.service';

@Component({
  selector: 'app-temp-hum',
  templateUrl: './temp-hum.component.html',
  styleUrls: ['./temp-hum.component.css'],
  standalone: true
})
export class TempHumComponent implements OnInit {
  temperature: number = 0;
  humidity: number = 0;

  constructor(private tempHumService: TempHumService) { }

  ngOnInit(): void {
    this.tempHumService.getTemperatureHumidity().then(
      data => {
        this.temperature = data.temperature;
        this.humidity = data.humidity;
      }
    );
  }
}
