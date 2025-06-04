import argparse
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import cm


def main(ticker: str):
    data = yf.download(ticker, period="30d", interval="1d")
    closing = data["Close"]
    if closing.empty:
        print(f"No data found for ticker {ticker}")
        return

    # replicate closing prices along Y-axis to create a surface
    z = np.tile(closing.values, (30, 1))
    x = np.arange(len(closing))
    y = np.arange(z.shape[0])
    X, Y = np.meshgrid(x, y)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection="3d")
    surf = ax.plot_surface(X, Y, z, cmap=cm.viridis, linewidth=0, antialiased=False)

    ax.set_xlabel("Days")
    ax.set_ylabel("Replication")
    ax.set_zlabel("Close Price")
    ax.set_title(f"30-Day Topographic Map for {ticker.upper()}")
    fig.colorbar(surf, shrink=0.5, aspect=10)

    output = f"{ticker}_topo.png"
    plt.tight_layout()
    plt.savefig(output)
    print(f"Saved {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create 3D topographic map for a stock ticker")
    parser.add_argument("ticker", help="Stock ticker symbol e.g. AAPL")
    args = parser.parse_args()
    main(args.ticker)
