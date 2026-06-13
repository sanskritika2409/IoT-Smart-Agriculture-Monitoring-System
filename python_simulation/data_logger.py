import pandas as pd
import os

FILE = "data/sensor_data.csv"

def save_data(data):
    df = pd.DataFrame([data])

    if os.path.exists(FILE) and os.path.getsize(FILE) > 0:
        df.to_csv(FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(FILE, index=False)