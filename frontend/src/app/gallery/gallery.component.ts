import { Component, OnInit, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  standalone: true,
  styleUrls: ['./gallery.component.scss']
})

export class GalleryComponent implements OnInit, OnDestroy {
  images: string[] = [
    'assets/foto/foto1.jpg',
    'assets/foto/foto2.jpg',
    'assets/foto/foto3.jpg',
    'assets/foto/foto4.jpg',
    'assets/foto/foto5.jpg',
    'assets/foto/foto6.jpg',
    'assets/foto/foto7.jpg'
  ];
  currentIndex: number = 0;
  currentImage: string = this.images[0];
  private intervalId: any;

  ngOnInit(): void {
    this.startSlideshow();
  }

  ngOnDestroy(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId); // Zatrzymanie interwału przy zniszczeniu komponentu
    }
  }

  startSlideshow(): void {
    this.intervalId = setInterval(() => {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
      this.currentImage = this.images[this.currentIndex];
    }, 6000); // Zmiana zdjęcia co 60000 ms (1 minuta)
  }
}
