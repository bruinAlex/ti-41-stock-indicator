# TI-42 Stock Indicator
## Introduction
This calculates the TI-42 metric for large numbers of tickers. TI-42 is a backward-looking breadth metric for timing entry/exit in a security. It is calculated by dividing the 4-day SMA by the 42-day SMA. Other periods could be used if desired.

## Requirements
- Python 3.7
- yfinance 0.1.54
- Pandas 1.0.3

## TODO
- Add argparse to feed in ticker list from a text file
- Output to .csv 
- Integrate with other indicators
