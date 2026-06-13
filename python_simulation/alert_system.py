def check_alerts(data):
    alerts = []

    if data["soil_moisture"] < 40:
        alerts.append("LOW SOIL MOISTURE - PUMP ON")

    if data["temperature"] > 35:
        alerts.append("HIGH TEMPERATURE ALERT")

    if data["water_level"] < 20:
        alerts.append("LOW WATER LEVEL ALERT")

    return alerts