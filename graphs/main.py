#!/usr/bin/env python3

from dataloader import load, get_stations
from graph import generate
from preprocessor import for_1d, for_7d

from datetime import datetime
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate athocs graphs")
    parser.add_argument("--station", type=str, default="all", help="ID of the station")
    parser.add_argument("--interval", type=str, choices=["1d", "7d"], required=True, help="Time interval (valid values: 1d, 7d)")
    parser.add_argument("--output-dir", type=str, default=".", help="Directory to save the graphs into")
    parser.add_argument("--api-host", type=str, default="192.168.0.86:1111", help="Hostname/IP and port of the API")
    parser.add_argument("--average", action="store_true", help="Include average calculation")
    
    args = parser.parse_args()

    hours = None
    xticks = None
    title_interval = None
    preprocess = None

    # no match-case for now because of ancient packages on debian
    if args.interval == "1d":
        if args.average: hours = 7 * 24
        else: hours = 24
        xticks = 1
        title_interval = "24 Hours"
        preprocess = for_1d

    if args.interval == "7d":
        hours = 7 * 24
        xticks = 4
        title_interval = "7 Days (smoothed)"
        preprocess = for_7d

    stations = [args.station]
    if args.station == "all":
        try:
            stations = get_stations(args.api_host)
        except Exception as e:
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("Loading stations list failed")
            print(e)
            print()
            sys.exit(1)

    for st in stations:
        try:
            data = load(args.api_host, st, hours=hours)
        except Exception as e:
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print(f"Loading the data for {st} failed")
            print(e)
            continue

        data, avg_data = preprocess(data, average=args.average)

        if len(data) == 0 and len(avg_data) == 0:
            print("Dataset length is 0, canceling graph generation")
            return

        generate(data, avg_data, f"{args.output_dir}/{st}-{args.interval}{'' if not args.average else '-avg'}.png", f"Temperature, Humidity and Pressure in the Last {title_interval}{'' if not args.average else ' (with average of last 7 days)'} at {st}", xticks)

