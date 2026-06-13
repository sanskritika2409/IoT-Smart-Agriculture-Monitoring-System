from python_simulation.sensor_simulator import generate_sensor_data
from python_simulation.alert_system import check_alerts
from python_simulation.data_logger import save_data

data = generate_sensor_data()

print("\nSMART AGRICULTURE MONITORING SYSTEM\n")
print(data)

alerts = check_alerts(data)

if alerts:
    print("\nALERTS:")
    for alert in alerts:
        print(alert)

save_data(data)