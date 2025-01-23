from flask import Flask, jsonify
from flask_cors import CORS

import time
import sqlite3
import datetime

try:
    import RPi.GPIO as GPIO
except ImportError:
    from fake_GPIO import GPIO

try:
    import dht11
except ImportError:
    from fake_adafruit_dht import DHT as Adafruit_DHT

app = Flask(__name__)
CORS(app)

# Konfiguracja czujnika i pinów LED
SENSOR = Adafruit_DHT.DHT11
SENSOR_PIN = 4  # Pin GPIO dla czujnika
LED_PINS = {'red': 17, 'green': 27, 'blue': 22}  # Przykładowe GPIO dla LED

GPIO.setmode(GPIO.BCM)
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)


@app.route('/data', methods=['GET'])
def get_sample_data():
    sample_data = {
        'temperature': 22.5,
        'humidity': 60
    }
    return jsonify(sample_data)


@app.route('/temperature', methods=['GET'])
def get_temperature():
    conn = sqlite3.connect('temphum_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM temphum ORDER BY id DESC LIMIT 1")
    conn.close()


# @app.route('/led', methods=['POST'])
# def set_led_color():
#     data = request.json
#     color = data.get('color')
#     if color in LED_PINS:
#         GPIO.output(LED_PINS[color], GPIO.HIGH)
#         return jsonify({'status': f'{color} LED turned on'})
#     return jsonify({'error': 'Invalid color'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    conn = sqlite3.connect('temphum_data.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS temphum
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       znacznik_czasowy TEXT,
                       hum NUMBER,
                       temp NUMBER)''')

    GPIO.setmode(GPIO.BCM)
    pin = 2
    sensor = dht11.DHT11(pin=pin)

    while True:
        result = sensor.read()
        if result.is_valid():  # Only process valid results
            x = result.humidity
            y = result.temperature
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO temphum (znacznik_czasowy, hum, temp) VALUES (?, ?, ?)", (now, x, y))
            conn.commit()
            time.sleep(60)

conn.close()
