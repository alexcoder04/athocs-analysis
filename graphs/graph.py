import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

def generate(data, data_avg, out_file: str, title: str, xticks: int):
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # temperature
    ax1.plot(data["timestamp"], data["temperature"], label="Temperature (°C)", color="red")
    if data_avg is not None:
        ax1.plot(data_avg["timestamp"], data_avg["temperature"], label="Temperature (°C) average", color="red", alpha=0.4)
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Temperature (°C)", color="red")
    ax1.tick_params(axis="y", labelcolor="red")

    # humidity
    ax2 = ax1.twinx()
    ax2.plot(data["timestamp"], data["humidity"], label="Humidity (%)", color="blue")
    if data_avg is not None:
        ax2.plot(data_avg["timestamp"], data_avg["humidity"], label="Humidity (%) average", color="blue", alpha=0.4)
    ax2.set_ylabel("Humidity (%)", color="blue")
    ax2.tick_params(axis="y", labelcolor="blue")

    # air pressure
    ax3 = ax1.twinx()
    ax3.spines["right"].set_position(("outward", 60))  # Offset the third axis
    ax3.plot(data["timestamp"], data["pressure"], label="Pressure (hPa)", color="green", alpha=0.25)
    ax3.set_ylabel("Pressure (hPa)", color="green")
    ax3.tick_params(axis="y", labelcolor="green")

    # x-axis - month-date hour:minute
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d %H:%M"))
    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=xticks))
    ax1.tick_params("x", rotation=90)

    # title and adjust
    plt.title(title)
    fig.tight_layout()

    plt.savefig(out_file)

