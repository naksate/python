import os
import time
import datetime
from binance.client import Client
from binance.helpers import round_step_size
import numpy as np
import time


# API Keys
api_key = ''
api_secret = ''

# Connect to client
client = Client(api_key, api_secret)

# CONSTANTS
symbol = 'FTMUSDT'
monnaie = 'FTM'
timeframe = '1m'
ema20_period = 20
ema50_period = 50
ema200_period = 200
precision = 8
tick_size = 1.00000000
step_size = 1.00000000
time_sleep = 65


#TEST / GET PRICE
print("TEST")
ticker = client.get_symbol_ticker(symbol=symbol)
print(ticker)
print("-----------------------------------")
price = float(ticker['price'])


# VERIFY QUANTITY AVAILABLE IN ACCOUNT
account_info = client.get_account()
balance_available = float([a['free'] for a in account_info['balances'] if a['asset'] == (monnaie)][0])
amount = balance_available
amt_str = "{:0.0{}f}".format(amount, precision)
rounded_amount = round_step_size(amt_str, tick_size)
print("Vérification de", monnaie, "dans le compte...")


while True:

    # VERIFY QUANTITY AVAILABLE IN ACCOUNT
    account_info = client.get_account()
    balance_available = float([a['free'] for a in account_info['balances'] if a['asset'] == (monnaie)][0])
    amount = balance_available
    amt_str = "{:0.0{}f}".format(amount, precision)
    rounded_amount = round_step_size(amt_str, tick_size)


    if balance_available >10:
            
        while True:
            
        # GET PRICE
            ticker = client.get_symbol_ticker(symbol=symbol)
            price = float(ticker['price'])

            # GET PRICE
            bars = client.get_historical_klines(symbol, timeframe,)

            # EXTRACT CLOSING PRICES
            closing_prices = np.array([float(bar[4]) for bar in bars])

            # CALCULATE EMAs
            ema20 = []
            ema50 = []
            ema200 = []

            for i in range(len(closing_prices)):
                if i == 0:
                    ema20.append(closing_prices[0])
                    ema50.append(closing_prices[0])
                    ema200.append(closing_prices[0])
                else:
                    ema20.append(((ema20_period - 1) * ema20[-1] + 2 * closing_prices[i]) / (ema20_period + 1))
                    ema50.append(((ema50_period - 1) * ema50[-1] + 2 * closing_prices[i]) / (ema50_period + 1))
                    ema200.append(((ema200_period - 1) * ema200[-1] + 2 * closing_prices[i]) / (ema200_period + 1))

            # GET LAST EMAs VALUES
            ema20_current = ema20[-1]
            ema50_current = ema50[-1]
            ema200_current = ema200[-1]

            print(monnaie, "disponibles dans le compte:", rounded_amount)
            print("En attente de validation de condition pour la vente")

            #print("EMA20:", ema20_current)
            #print("EMA20:", ema50_current)
            #print("EMA20:", ema200_current)
            
            if ema20_current < ema50_current:
                    order = client.order_market_sell(
                    symbol= symbol,
                    quantity=rounded_amount)
                    print("Ordre de vente de:", rounded_amount, "passé avec succès!")
                    print("Vente: ", rounded_amount*price, "USDT")
                    amount_sold = []
                    amount_sold = rounded_amount
                    break
            
            else: 
                print("Pause de", time_sleep, "secondes, condition non réunie")
                print("-----------------------------------")
                time.sleep(time_sleep)





    else:
         
         print(monnaie, "non disponibles dans le compte")
         print("-----------------------------------")
         
         #GET LAST QUANTITY BOUGHT IN USDT
         orders = client.get_all_orders(symbol=symbol)
         last_quantity_usdt = float(orders[-1]['cummulativeQuoteQty']) - 0.001*float(orders[-1]['cummulativeQuoteQty'])

         while True: 

            #GET PRICE
            ticker = client.get_symbol_ticker(symbol=symbol)
            price = float(ticker['price'])
        
            # CALCULATE QUANTITY TO BUY
            quantity = float(last_quantity_usdt / price)
            amt_str = float("{:0.0{}f}".format(quantity, precision))
            rounded_amount = round_step_size(amt_str, tick_size)

            # GET PRICE DATA
            bars = client.get_historical_klines(symbol, timeframe,)

            # EXTRACT CLOSING PRICES
            closing_prices = np.array([float(bar[4]) for bar in bars])

            # CALCULATE EMAs
            ema20 = []
            ema50 = []
            ema200 = []

            for i in range(len(closing_prices)):
                if i == 0:
                    ema20.append(closing_prices[0])
                    ema50.append(closing_prices[0])
                    ema200.append(closing_prices[0])
                else:
                    ema20.append(((ema20_period - 1) * ema20[-1] + 2 * closing_prices[i]) / (ema20_period + 1))
                    ema50.append(((ema50_period - 1) * ema50[-1] + 2 * closing_prices[i]) / (ema50_period + 1))
                    ema200.append(((ema200_period - 1) * ema200[-1] + 2 * closing_prices[i]) / (ema200_period + 1))

            # GET LAST EMAs VALUES
            ema20_current = ema20[-1]
            ema50_current = ema50[-1]
            ema200_current = ema200[-1]


            print("Quantité de", monnaie," prêts à être achetés:", rounded_amount, "au prix de", price, "soit", last_quantity_usdt, "USDT")
            print("En attente de validation des conditions pour l'achat...")
            
            # VERIFY CONDITIONS OF PURCHASE
            if ema20_current > ema50_current: 

                    # PLACE BUY ORDER
                    order = client.order_market_buy(
                    symbol=symbol,
                    quantity=rounded_amount)
                    print("Ordre d'achat de", rounded_amount, "au prix de", price, "passé avec succès!")
                    print("Pause de 15 secondes, calcul de quantité à vendre")
                    time.sleep(15)
                    break
            else: 
                print("Pause de", time_sleep, "secondes, condition non réunie")
                print("-----------------------------------")
                time.sleep(time_sleep)

