#!/usr/bin/env python3

from dataloader import load
from graph import generate
from preprocessor import for_1d, for_7d

import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate athocs graphs")
    parser.add_argument("--station", type=str, required=True, help="ID of the station")
    parser.add_argument("--interval", type=str, choices=["1d", "7d"], required=True, help="Time interval (valid values: 1d, 7d)")
    parser.add_argument("--output-dir", type=str, default=".", help="Directory to save the graphs into")
    parser.add_argument("--api-host", type=str, default="192.168.0.86:1111", help="Hostname/IP and port of the API")
    parser.add_argument("--average", action="store_true", help="Include average calculation")
    
    args = parser.parse_args()

    hours = None
    xticks = None
    title_interval = None
    preprocess = None
    match args.interval:
        case "1d":
            if args.average: hours = 7 * 24
            else: hours = 24
            xticks = 1
            title_interval = "24 Hours"
            preprocess = for_1d
        case "7d":
            hours = 7 * 24
            xticks = 4
            title_interval = "7 Days (smoothed)"
            preprocess = for_7d

    try:
        data = load(args.api_host, args.station, hours=hours)
    except Exception as e:
        print("Loading the data failed")
        print(e)

    data, avg_data = preprocess(data, average=args.average)

    generate(data, avg_data, f"{args.output_dir}/{args.interval}{'' if not args.average else '-avg'}.png", f"Temperature, Humidity and Pressure in the Last {title_interval}{'' if not args.average else ' (with average of last 7 days)'}", xticks)

