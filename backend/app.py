import threading
import datetime
import pytz
import sqlite3
import time
from flask import Flask, jsonify
from flask_cors import CORS
import asyncio
from bleak import BleakClient

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
    data = cursor.fetchone()
    conn.close()
    sample_data = {
        'temperature': data[3],
        'humidity': data[2]
    }
    return jsonify(sample_data)


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


    while True:
        result = sensor.read()
        while not result.is_valid():
            result = sensor.read()
            time.sleep(1)

        x = result.humidity
        y = result.temperature
        now = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO temphum (znacznik_czasowy, hum, temp) VALUES (?, ?, ?)", (now, x, y))
        conn.commit()
        print(f"Inserted data: {now}, {x}, {y}")
        time.sleep(60)

async def set_LED_color(address):
    async with BleakClient(address) as client:
        # różowy
        header = bytes.fromhex("7e07")
        command = bytes.fromhex("05")
        params = bytes.fromhex("03ff001310ef")

        # # czerwony
        # header = bytes.fromhex("7e07")
        # command = bytes.fromhex("05")
        # params = bytes.fromhex("0314000010ef")

        data = header + command + params
        # data = header + command + params + bytes.fromhex("ef")
        # data = bytes.fromhex("7e04010801ffff00ef")

        model_number = await client.write_gatt_char(
            "0000fff3-0000-1000-8000-00805f9b34fb",
            data
        )
        print("Data sent successfully.")
    asyncio.run(main(address))

if __name__ == '__main__':
    address = "be:27:11:00:56:c2"
    asyncio.run(set_LED_color(address))

    sensor_thread = threading.Thread(target=read_sensor_data)
    sensor_thread.start()
    app.run(host='0.0.0.0', port=5000)

