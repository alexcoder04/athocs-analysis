from datetime import datetime, timedelta
import pandas as pd


def load(api_host: str, station: str, hours: int = 24):
    ts_end = datetime.now()
    ts_start = ts_end - timedelta(hours=hours)

    input_url = f"http://{api_host}/api/data?station={station}&time_from={ts_start.strftime('%Y-%m-%d_%H:%M:%S')}&time_to={ts_end.strftime('%Y-%m-%d_%H:%M:%S')}"

    data = pd.read_csv(input_url)
    data["timestamp"] = pd.to_datetime(data["timestamp"], format='%Y-%m-%d_%H:%M:%S')

    return data


def get_stations(api_host: str):
    input_url = f"http://{api_host}/api/stations"
    return pd.read_csv(input_url)["id"].tolist()

