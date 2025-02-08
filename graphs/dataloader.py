from datetime import datetime, timedelta
import pandas as pd


def load(api_host: str, station: str, hours: int = 24):
    ts_end = datetime.now()
    ts_start = ts_end - timedelta(hours=hours)

    INPUT_URL = f"http://{api_host}/api/data?station={station}&time_from={ts_start.strftime('%Y-%m-%d_%H:%M:%S')}&time_to={ts_end.strftime('%Y-%m-%d_%H:%M:%S')}"

    data = pd.read_csv(INPUT_URL)
    data["timestamp"] = pd.to_datetime(data["timestamp"], format='%Y-%m-%d_%H:%M:%S')

    return data

