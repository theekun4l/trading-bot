allowed_symbols = [
    "BTCUSDT",
    "ETHUSDT",
    "BNBUSDT",
    "XRPUSDT",
    "SOLUSDT",
    "ADAUSDT"
]
def validate_symbol(symbol):
    if symbol not in allowed_symbols:
        raise ValueError(f"Invalid symbol. Allowed: {','.join(allowed_symbols)}")
    else:
        return True
def validate_side(side):
    if side not in ["BUY", "SELL"]:
        return False
    else:
        return True
def validate_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        return False
    else:
        return True
def validate_quantity(quantity):
   try:
       quantity = float(quantity)
       if quantity < 0:
           raise ValueError("Quantity cannot be negative")
       return True
   except:
        return False