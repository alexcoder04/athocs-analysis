from dataloader import load
from default_graph import generate

import matplotlib.dates as mdates
import os

if __name__ == "__main__":
    base_dir = os.getenv("ATHOCS_BASE_DIR")
    data = load(hours=7*24).drop(columns=["station"])
    data["timestamp"] = data["timestamp"].dt.floor("15min")
    data = data.groupby("timestamp").mean().reset_index()
    generate(data, f"{base_dir}/graphs/last-7d.png", title="Temperature, Humidity and Pressure in the Last 7 Days (smoothed)", xaxis_locator=mdates.HourLocator(interval=4))

