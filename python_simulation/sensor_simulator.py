import random

def generate_sensor_data():
    return {
        "soil_moisture": random.randint(20, 100),
        "temperature": random.randint(20, 45),
        "humidity": random.randint(30, 90),
        "light_intensity": random.randint(100, 1000),
        "water_level": random.randint(10, 100)
    }