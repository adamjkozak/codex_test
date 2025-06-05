import argparse
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import cm


def main(ticker: str):
    data = yf.download(
        ticker,
        period="30d",
        interval="1d",
        auto_adjust=False,
        progress=False,
    )

    if data.empty:
        print(f"No data found for ticker {ticker}")
        return

    # Ensure the required columns exist before processing
    if not {"Close", "Volume"}.issubset(data.columns):
        print(f"No data found for ticker {ticker}")
        return

    data = data[["Close", "Volume"]].dropna()
    if data.empty:
        print(f"No data found for ticker {ticker}")
        return

    closing = data["Close"].values
    volume = data["Volume"].values

    n = len(closing)
    x = np.arange(n)
    X = np.tile(x, (n, 1))
    Y = np.tile(volume.reshape(-1, 1), (1, n))
    z = np.tile(closing, (n, 1))

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection="3d")
    surf = ax.plot_surface(
        X,
        Y,
        z,
        cmap=cm.viridis,
        linewidth=0,
        antialiased=False,
    )

    ax.set_xlabel("Days")
    ax.set_ylabel("Trading Volume")
    ax.set_zlabel("Close Price")
    ax.set_title(f"30-Day Topographic Map for {ticker.upper()}")
    fig.colorbar(surf, shrink=0.5, aspect=10)

    output = f"{ticker}_topo.png"
    plt.tight_layout()
    plt.savefig(output)
    print(f"Saved {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create 3D topographic map for a stock ticker",
    )
    parser.add_argument("ticker", help="Stock ticker symbol e.g. AAPL")
    args = parser.parse_args()
    main(args.ticker)
