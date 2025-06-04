# Stock Topographic Map App

This repository includes a simple command line tool that generates a 3D topographic map of the closing prices for a stock ticker over the last 30 days.

## Requirements

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with a ticker symbol:

```bash
python stock_topomap.py AAPL
```

The script downloads the past 30 days of daily data and outputs an image named `<TICKER>_topo.png` in the current directory.

