import time
import requests

INFLUXDB_URL = 'http://influxdb:8086/api/v2/write?org=ZHAW&bucket=raspberrypi&precision=s'
INFLUXDB_TOKEN = 'NN04S8ycrz5EaAxJQhznlfHoV8dmf-Nhuc8hsBhx9ijnnWUrg61HbYCju8bzRyA6hrm0WGixqGWKpbr0iwIoNQ=='

def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read()) / 1000  # Convert milliCelsius to Celsius
            return temp
    except FileNotFoundError:
        print("Error: Could not find /sys/class/thermal/thermal_zone0/temp")
        return None

def get_cpu_utilization():
    with open("/proc/stat", "r") as f:
        cpu_line = f.readline().split()
    user, nice, system, idle, *_ = cpu_line[1:]
    idle_time = int(idle)
    busy_time = int(user) + int(nice) + int(system)
    total_time = idle_time + busy_time
    cpu_utilization = 100.0 * (busy_time / total_time)
    return cpu_utilization

def send_to_influxdb(temp, cpu_usage):
    data = f"temperature value={temp}\ncpu_usage value={cpu_usage}"
    headers = {
        'Authorization': f'Token {INFLUXDB_TOKEN}',
        'Content-Type': 'text/plain; charset=utf-8',
    }
    response = requests.post(INFLUXDB_URL, data=data, headers=headers)
    if response.status_code != 204:
        print(f"Failed to send data to InfluxDB: {response.text}")
    else:
        print(f"Successfully sent data to InfluxDB: {data}")

def main():
    while True:
        temp = get_cpu_temp()
        if temp is not None:
            print(f"CPU Temperature: {temp}°C")
        else:
            print("Failed to read CPU temperature.")
        cpu_usage = get_cpu_utilization()
        print(f"CPU Utilization: {cpu_usage:.1f}%")
        if temp is not None:
            send_to_influxdb(temp, cpu_usage)
        time.sleep(10)  # collect data every 10 seconds

if __name__ == "__main__":
    main()
