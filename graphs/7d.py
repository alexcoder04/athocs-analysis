from dataloader import load
from default_graph import generate

import matplotlib.dates as mdates
import os

if __name__ == "__main__":
    base_dir = os.getenv("ATHOCS_BASE_DIR")
    data = load(hours=7*24)
    generate(data, f"{base_dir}/graphs/last-7d.png", xaxis_locator=mdates.HourLocator(interval=4))

