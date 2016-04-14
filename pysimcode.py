
# THIS IS WHERE THE CODE FOR THE ALGORITHM GOES. All the code you wish
# to backtest goes in this file. The code below will be executed for all
# the existing records (days) of S&P 500 stocks from 1998 - 2013. In other words,
# it will be executed EVERY DAY from 1998 to 2013 on ALL of the stocks.

# VARIABLES THAT YOU CAN USE:
# ticker (the stock's ticker, used for purchasing or selling)
# open_price (the stock's opening price of the day)
# close_price (the stock's closing price of the day)
# high (the stock's high price of the day)
# low (the stock's low price of the day)
# vol (the stock's volume)
# account (your bank account)
# transaction_fee

# BESIDE THESE VALUES, you can use your own variables to keep track of any
# averages, or simply variables you want to remember. Write these variables in
# the "init" section. The "init" function will be called for every separate ticker

# HOW TO PURCHASE/SELL
# To purchase or sell any stocks: account.sellStock(ticker, quantity_desired, price)
# OR account.buyStock(ticker, quantity_desired, price). Note that "ticker" is already provided
# to you as a variable, but you must provide the quantity desired and the price. For price,
# you should use any of the price-related variables provided above. "account" will
# perform erroneously if you attempt to sell stock you don't own, or more than you
# own. Refer to the pybank.py documentation.

# REMEMBER
# remember to take into account your funds - you cannot continue buying
# forever, or the account will throw an error. Refer to the documentation of
# pybank

# should RETURN a dictionary of optional variables, if needed
def init():
    return {}

# the main algorithm that will be run for each stock, every day
def main(account, ticker, open_price, close_price, high, low, vol, transaction_fee, optional_variables={}):
    if ticker == "AAPL" and ticker not in account.getStocks():
        if account.getValue() - ((100 * open_price) + transaction_fee) >= 0:
            account.buyStock(ticker, 100, open_price)
