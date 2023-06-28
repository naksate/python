# 2 EMAs strategy trading bot

A python script that calculates the EMA 20 and EMA 50 of a PAIR and BUYS when EMA 20 > EMA 50 and SELLS when EMA 20 < EMA 50

# How it works

- Quantity must be > 10 in order to BUY or SELL
- Checks the quantity available of the PAIR you want to trade
- If quantity > 10, calculates the EMAs at the timeframe you decided and checks if it can sell 
- If quantity < 10, gets last quantity bought of the coin and verifies if it can buy
- If one of the conditions is met, the script will automatically verify the other condition

# Must know

- The "tick_size" and "step_size" are different for every PAIRS




