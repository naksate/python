# 2 EMAs Strategy Trading Bot

A Python script that calculates the EMA 20 and EMA 50 of a PAIR and BUYS when EMA 20 > EMA 50 and SELLS when EMA 20 < EMA 50.

# How it works

- Quantity must be > 10 in order to BUY or SELL.
- Checks the available quantity of the PAIR you want to trade.
- If the quantity is > 10, it calculates the EMAs at the timeframe you have chosen and checks if it can be sold.
- If the quantity is < 10, it retrieves the last purchased quantity of the coin, calculates the EMAs and verifies if it can be bought.
- If one of the conditions is met, the script will automatically verify the other condition.

# Important Note

- The values for "tick_size" and "step_size" vary for each PAIR and must be adjusted accordingly.




