import threading
import datetime
import pytz
import sqlite3
import time
from flask import Flask, jsonify
from flask_cors import CORS

try:
    import RPi.GPIO as GPIO
except ImportError:
    from fake_GPIO import GPIO

try:
    import dht11
except ImportError:
    from fake_adafruit_dht import DHT as Adafruit_DHT

# Define the time zone
timezone = pytz.timezone('Europe/Warsaw')

app = Flask(__name__)
CORS(app)

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
def read_sensor_data():
    GPIO.setmode(GPIO.BCM)
    pin = 2
    sensor = dht11.DHT11(pin=pin)

    conn = sqlite3.connect('temphum_data.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS temphum
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       znacznik_czasowy TEXT,
                       hum NUMBER,
                       temp NUMBER)''')

    for j in range(10):
        result = sensor.read()
        if result.is_valid():  # Only process valid results
            x = result.humidity
            y = result.temperature
            now = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO temphum (znacznik_czasowy, hum, temp) VALUES (?, ?, ?)", (now, x, y))
            conn.commit()
            print(f"Inserted data: {now}, {x}, {y}")
        else:
            print("Invalid sensor reading")
        time.sleep(60)

    conn.close()

if __name__ == '__main__':
    sensor_thread = threading.Thread(target=read_sensor_data)
    sensor_thread.start()
    app.run(host='0.0.0.0', port=5000)

