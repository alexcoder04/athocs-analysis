import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

def generate(data, data_avg, out_file, title="Temperature, Humidity, and Pressure in the Last 24 Hours (with average of last 7 days)", xaxis_locator=mdates.HourLocator(interval=1)):
    # Create a figure and axis for the plot
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot temperature on the first y-axis
    ax1.plot(data["timestamp"], data["temperature"], label="Temperature (°C)", color="red")
    ax1.plot(data_avg["timestamp"], data_avg["temperature"], label="Temperature (°C) average", color="red", alpha=0.4)
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Temperature (°C)", color="red")
    ax1.tick_params(axis="y", labelcolor="red")

    # Create a second y-axis for humidity
    ax2 = ax1.twinx()
    ax2.plot(data["timestamp"], data["humidity"], label="Humidity (%)", color="blue")
    ax2.plot(data_avg["timestamp"], data_avg["humidity"], label="Humidity (%) average", color="blue", alpha=0.4)
    ax2.set_ylabel("Humidity (%)", color="blue")
    ax2.tick_params(axis="y", labelcolor="blue")

    # Format the x-axis to show month-date hour:minute and display every hour
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d %H:%M"))
    ax1.xaxis.set_major_locator(xaxis_locator)
    ax1.tick_params("x", rotation=90)

    # Add a title and adjust layout
    plt.title(title)
    fig.tight_layout()

    # Save the plot as an image
    plt.savefig(out_file)

