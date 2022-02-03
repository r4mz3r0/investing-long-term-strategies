# Install Robinhood python framework https://github.com/LichAmnesia/Robinhood 
from Robinhood import Robinhood 

#Log into robinhood
robinhood_client = Robinhood()
robinhood_client.login(username="youremailhere@mail.com", password="yourpasswordhere") 

# 2 Factor authentication 
QR = "1234567890qwerty"
my_trader = Robinhood()
my_trader.login(username="username", password="password", qr_code=QR)
#Get recent Amazon stock price 
stock_instrument = my_trader.instruments("AMZN")[0]
AMZN_PRICE = my_trader.quote_data("AMZN")

# Buy and hold
while(AMZN_PRICE != -69):
  buy_order = my_trader.place_market_buy_order(stock_instrument["url], "AMZN", "GFD", 1)
