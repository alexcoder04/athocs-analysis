import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

def generate(data, out_file, xaxis_locator=mdates.HourLocator(interval=1)):
    # Create a figure and axis for the plot
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot temperature on the first y-axis
    ax1.plot(data["timestamp"], data["temperature"], label="Temperature (°C)", color="red")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Temperature (°C)", color="red")
    ax1.tick_params(axis="y", labelcolor="red")

    # Create a second y-axis for humidity
    ax2 = ax1.twinx()
    ax2.plot(data["timestamp"], data["humidity"], label="Humidity (%)", color="blue")
    ax2.set_ylabel("Humidity (%)", color="blue")
    ax2.tick_params(axis="y", labelcolor="blue")

    # Create a third y-axis for pressure
    ax3 = ax1.twinx()
    ax3.spines["right"].set_position(("outward", 60))  # Offset the third axis
    ax3.plot(data["timestamp"], data["pressure"], label="Pressure (hPa)", color="green", alpha=0.25)
    ax3.set_ylabel("Pressure (hPa)", color="green")
    ax3.tick_params(axis="y", labelcolor="green")

    # Format the x-axis to show month-date hour:minute and display every hour
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d %H:%M"))
    ax1.xaxis.set_major_locator(xaxis_locator)
    ax1.tick_params("x", rotation=90)

    # Add a title and adjust layout
    plt.title("Temperature, Humidity, and Pressure in the Last 24 Hours")
    fig.tight_layout()

    # Save the plot as an image
    plt.savefig(out_file)

