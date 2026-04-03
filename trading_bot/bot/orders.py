def order(symbol, side, qty,order_id,price,limit_price,status):
    return {
        "OrderID" : order_id,
        "symbol": symbol,
        "side": side,
        "quantity": qty,
        'limit Price': limit_price,
        "price": price,
        "status": status
    }