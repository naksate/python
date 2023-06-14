# 2 EMAs strategy trading bot

A python program that calculates the EMA 20 and EMA 50 of a coin and BUYS when EMA 20 > EMA 50 and SELLS when EMA 50 < EMA 20

# How it works

- Checks the quantity available of the coin you want to trade
- If quantity > 10, calculates the EMAs at the timeframe you decided and checks if it can sell 
- If quantity < 10, gets last quantity bought of the coin and checks if it can buy
- If one of the conditions , it will automatically verify the other condition

# Must change



# Must know

- Quantity must be > 10 in order to BUY or SELL
