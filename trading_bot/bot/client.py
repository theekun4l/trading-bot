import requests
class BinanceClient:
    BASE_URL = "https://testnet.binancefuture.com"
    def get_price(self, symbol):
        url = f"{self.BASE_URL}/fapi/v1/ticker/price"
        params = {"symbol": symbol}
        response = requests.get(url, params=params)
        return response.json()
    def place_order(self, data):
        return {
            "orderID": data['OrderID'],
            "symbol": data['symbol'],
            "side": data['side'],
            "status": data['status'],
            "executedQty": data['quantity'],
            "avgPrice": data['price'],
            "limit_price": data['limit Price']

        }
