// temp-hum.service.ts
// temp-hum.service.ts
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TempHumService {
  private baseUrl = 'http://localhost:5000/temperature';

  constructor() { }

  async getTemperatureHumidity(): Promise<any> {
    const response = await fetch(this.baseUrl);
    const data = await response.json();
    console.log('Received data:', data);
    return data;
  }
}
