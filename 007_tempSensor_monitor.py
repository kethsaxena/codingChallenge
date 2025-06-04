import time
import random
import os
import psutil
import datetime
import json

def simulate_temperature_sensor(sensor_id="sensor_02_py", mean_temp=25.0, variation=2.0, interval=1.0):
    process = psutil.Process(os.getpid())

    try:
        while True:
            # Simulated sensor reading
            temp = random.normalvariate(mean_temp, variation)

            # Timestamp in ISO 8601 format with simulated nanoseconds
            now = datetime.datetime.utcnow()
            nanos = now.microsecond * 1000  # Convert microseconds to nanoseconds
            timestamp = now.strftime('%Y-%m-%dT%H:%M:%S') + f'.{nanos:09d}Z'

            # Resource usage
            cpu_percent = process.cpu_percent(interval=None)
            mem_info = process.memory_info()
            rss_mb = mem_info.rss / (1024 * 1024)

            # Print resource usage
            print(f"Memory Usage: {rss_mb:.2f} MB | CPU Usage: {cpu_percent:.2f}%")

            # Print sensor JSON
            sensor_data = {
                "sensor_id": sensor_id,
                "timestamp": timestamp,
                "temperature": f"{temp:.2f}°C"
            }
            print(json.dumps(sensor_data,ensure_ascii=False))

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nSensor simulation stopped.")

simulate_temperature_sensor()
