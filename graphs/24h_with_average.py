from dataloader import load
from graph_with_average import generate

from datetime import datetime, timedelta
import matplotlib.dates as mdates
import pandas as pd
import os

if __name__ == "__main__":
    base_dir = os.getenv("ATHOCS_BASE_DIR")

    ts_end = datetime.now()
    ts_start = ts_end - timedelta(hours=24)

    data_7d = load(hours=24*7)
    data = data_7d[data_7d["timestamp"].between(ts_start, ts_end)].drop(columns=["pressure"])

    data_7d = data_7d.drop(columns=["station","battery","pressure"])
    data_7d["timestamp"] = data_7d["timestamp"].dt.floor("15min").dt.strftime("%H:%M")
    data_7d = data_7d.groupby("timestamp").mean().reset_index()

    latest_date = data["timestamp"].max().date()
    data_7d["timestamp"] = pd.to_datetime(data_7d["timestamp"], format="%H:%M").apply(lambda x: x.replace(year=latest_date.year, month=latest_date.month, day=latest_date.day))
    data_7d.loc[data_7d["timestamp"] > data["timestamp"].max(), "timestamp"] -= pd.Timedelta(days=1)
    data_7d = data_7d.sort_values(by="timestamp")

    generate(data, data_7d, f"{base_dir}/graphs/last-24h-with-avg.png", xaxis_locator=mdates.HourLocator(interval=1))

