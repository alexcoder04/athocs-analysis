from datetime import datetime, timedelta
import pandas as pd
import os

def load(hours=24):
    ts_end = datetime.now()
    ts_start = ts_end - timedelta(hours=hours)

    IP = os.getenv("ATHOCS_IP")
    PORT = os.getenv("ATHOCS_PORT")

    STATION = "RPIZ-ALEX"

    INPUT_URL = f"http://{IP}:{PORT}/api/data?station={STATION}&time_from={ts_start.strftime('%Y-%m-%d_%H:%M:%S')}&time_to={ts_end.strftime('%Y-%m-%d_%H:%M:%S')}"

    data = pd.read_csv(INPUT_URL)
    # Ensure the timestamp column is in timestamp format
    data["timestamp"] = pd.to_datetime(data["timestamp"], format='%Y-%m-%d_%H:%M:%S')

    return data

