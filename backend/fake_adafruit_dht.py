class DHT:
    DHT11 = 11
    DHT22 = 22

    @staticmethod
    def read_retry(sensor, pin):
        print(f"Symulacja odczytu z czujnika na pinie {pin}")
        # Zwrot przykładowych danych (temperatura, wilgotność)
        return 22.5, 55.0
