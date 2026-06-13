from python_simulation.sensor_simulator import generate_sensor_data
from python_simulation.alert_system import check_alerts
from python_simulation.data_logger import save_data
import time

print("Smart Agriculture Monitoring Started...")

while True:

    data = generate_sensor_data()

    print(data)

    alerts = check_alerts(data)

    for alert in alerts:
        print(alert)

    save_data(data)

    time.sleep(5)