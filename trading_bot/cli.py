from bot.validators import validate_symbol, validate_side, validate_type, validate_quantity
from bot.orders import order
from bot.client import BinanceClient
from bot.logging_config import setup_logger
import logging

setup_logger()
logging.info("Application started")

client = BinanceClient() #object of binance class
order_id = 0

def menu():
    print('\n===Binance Futures CLI===')
    print('[1] Place Order')
    print('[2] Check Current Price')
    print('[3] Exit')
def confirm_user():
    while True:
        confirm = input("Confirm Purchase? (y/n) ").lower()
        if confirm == "y":
            return True
        elif confirm == "n":
            return False
        else:
            print("Invalid Input")
            logging.warning("Invalid Input")
            continue
def get_valid_input(prompt,validator):
    while True:
        value = input(prompt).upper()
        if value == "":
            print('\nGoing back to main menu...')
            logging.info("Going back to main menu...")
            return
        try:
            if validator(value):
                return value
            else:
                print('Invalid Input')
                logging.warning("Invalid Input")
        except ValueError as e:
            print(e)
            logging.error(e)
def get_valid_float(prompt,validator):
    while True:
        value = input(prompt)
        if value == "":
            print('\nGoing back to main menu...')
            logging.info("Going back to main menu...")
            return
        try:
            if validator(value):
                return value
            else:
                print('Invalid Input')
                logging.warning("Invalid Input")
        except ValueError as e:
            print(e)
            logging.error(e)
def handle_order_type(type1,side,symbol):
    current_price = float(client.get_price(symbol)['price'])
    if type1 == 'MARKET':
        qty = get_valid_float("Quantity (eg., 0.001):", validate_quantity)
        if not qty:
            return
        net_price = (current_price) * float(qty)
        print(f"Net purchase is: {round(net_price, 2)}")
        if confirm_user():
            return net_price, side, 'FILLED',qty
        else:
            logging.info("User cancelled the order")
            return
    elif type1 == 'LIMIT':
        while True:
            print(f"Current Price is: {round(current_price, 2)}")
            if side == 'BUY':
                limit_price = get_valid_float("Enter the limit price (e.g. Lesser than current price):",
                                              validate_quantity)
                limit_price = float(limit_price)
                qty = get_valid_float("Quantity (eg., 0.001):", validate_quantity)
                if not qty:
                    return
                net_price = current_price * float(qty)
                if limit_price < current_price:
                    return net_price, limit_price, 'OPEN (waiting for price drop)',qty
                elif limit_price > current_price:
                    print("Warning: Price is higher than current market price. Order may execute immediately.")
                    logging.warning("Limit price is higher than market -> may execute immediately.")
                    if confirm_user():
                        return net_price, limit_price, 'FILLED',qty
                    else:
                        logging.info("User cancelled the order")
                        return
                else:
                    print("Limit price is equal to current market price. Order may execute immediately.")
                    if confirm_user():
                        return net_price, limit_price, 'FILLED',qty
                    else:
                        logging.info("User cancelled the order")
                        return
            else:
                limit_price = get_valid_float("Enter the limit price (e.g. Higher than current price):",
                                              validate_quantity)
                limit_price = float(limit_price)
                qty = get_valid_float("Quantity (eg., 0.001):", validate_quantity)
                if not qty:
                    return
                net_price = float(current_price) * float(qty)
                if limit_price < current_price:
                    print("Warning: Price is Lower than current market price. Order may execute immediately.")
                    logging.warning("Limit price is Lower than market -> may execute immediately.")
                    if confirm_user():
                        return net_price, limit_price, 'FILLED',qty
                    else:
                        logging.info("User cancelled the order")
                        return
                elif limit_price > current_price:
                    return net_price, limit_price, 'OPEN (waiting for price up)',qty
                else:
                    print("Limit price is equal to current market price. Order may execute immediately.")
                    if confirm_user():
                        return net_price, limit_price, 'FILLED',qty
                    else:
                        logging.info("User cancelled the order")
                        return

def place_order():
       logging.info("Order process started")
       global order_id
       symbol = get_valid_input("Symbol (BTCUSDT/ETHUSDT) or Enter to go back :",validate_symbol)
       logging.info(f"Symbol selected: {symbol}")
       if not symbol:
           return
       current_price = float(client.get_price(symbol)['price'])
       print(f"Symbol : {symbol}")
       print(f"Current price: {current_price}")
       side = get_valid_input("Side [BUY / SELL] or Enter to go back:",validate_side)
       logging.info(f"Side selected: {side}")
       if not side:
           return
       order_type = get_valid_input("Order Type [MARKET / LIMIT] or Enter to go back:",validate_type)
       logging.info(f"Order Type: {order_type}")
       if not order_type:
           return
       result = handle_order_type(order_type,side ,symbol)
       if not result:
           return
       net_price ,limit_price,status,qty = result
       order_id += 1
       O1 = order(symbol, side, qty,order_id,net_price,limit_price,status)
       data =  client.place_order(O1)
       logging.info(f"Order placed : {symbol},{side}, Qty : {qty},Status: {status}")
       print('Trade details:')
       for key, value in data.items():
           print(f"{key:<10} : {value}")
       input('Press any key to continue...')
       return
def check_price():
    while True:
        symbol = get_valid_input("Symbol (BTCUSDT/ETHUSDT) or Enter to go back:",validate_symbol)
        logging.info(f"Symbol selected: {symbol}")
        if not symbol:
            logging.info("Going back to menu...")
            return
        else:
            print('Information:')
            for key , value in client.get_price(symbol).items():
                print(f"{key:<10} : {value}")
            input('Press any key to continue...')
while True:
    menu()
    user_choice = input('Enter your choice(1/2/3): ')
    logging.info(f"User selected option : {user_choice}")
    if user_choice == '1':
        place_order()
    elif user_choice == '2':
        check_price()
    elif user_choice == '3':
        print('Goodbye...')
        logging.info('EXITING APPLICATION')
        break
    else:
        print('Invalid choice')
        logging.warning("User entered invalid choice")
        continue