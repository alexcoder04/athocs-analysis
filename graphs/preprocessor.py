from datetime import datetime, timedelta
import pandas as pd


def for_1d(data, average: bool = False):
    if not average:
        return data, None

    data_7d = data
    data_last_day = data[data["timestamp"] > (datetime.now() - timedelta(hours=24))]
    if len(data_last_day) == 0:
        return None, None

    latest_date = data_last_day["timestamp"].max().date()

    data_7d = data_7d.drop(columns=["station","battery","pressure"])
    data_7d["timestamp"] = data_7d["timestamp"].dt.floor("10min")
    data_7d["timestamp"] = data_7d["timestamp"].apply(lambda t: t.replace(year=latest_date.year, month=latest_date.month, day=latest_date.day))
    data_7d = data_7d.groupby("timestamp").mean().reset_index()
    data_7d.loc[data_7d["timestamp"] > data_last_day["timestamp"].max(), "timestamp"] -= pd.Timedelta(days=1)
    data_7d = data_7d.sort_values(by="timestamp")

    return data_last_day, data_7d


def for_7d(data, average: bool = False):
    data = data.drop(columns=["station"])
    data["timestamp"] = data["timestamp"].dt.floor("20min")
    data = data.groupby("timestamp").mean().reset_index()
    return data, None

