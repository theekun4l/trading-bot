Binance Futures CLI Trading Bot

Overview

This is a simple CLI-based trading bot built in Python.
It allows users to place MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- Input validation (symbol, side, order type, quantity, price)
- Order confirmation before execution
- Logging of important events and errors
- Check current market price

Project Structure

trading_bot/
│── bot/
│   ├── client.py          # Binance API interaction
│   ├── orders.py          # Order logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│── cli.py                 # Main CLI interface
│── requirements.txt
│── README.md

How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run the CLI:

python cli.py

Usage

- Select options from menu:
  - Place Order
  - Check Current Price
  - Exit
- Follow prompts to enter symbol, side, order type, etc.

Note

While attempting to use the Binance Futures Testnet, I encountered an issue with API key generation. 
The testnet activation page was not redirecting properly, which prevented access to API credentials.

As a result, the order execution is currently simulated. Despite this, the core trading logic (MARKET and LIMIT orders) has been fully implemented to reflect real-world behavior.

Logging

Logs are stored in a logging_config file which include:

- Order actions
- Warnings
- Errors

Author

Kunal Maheshwari
