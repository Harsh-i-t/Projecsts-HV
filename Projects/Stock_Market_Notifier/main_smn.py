import datetime
import time
from plyer import notification
import yfinance as yf
stock = yf.Ticker("GOOG")
data = stock.info

while True:
    notification.notify(
        title = 'Google Stock Data'.format(datetime.date.today()),
        message = 'Current Price = {cp} \nDayLow = {dl} \nDayHigh = {dh}'.format(
            cp = data["currentPrice"],
            dl = data["regularMarketDayLow"],
            dh = data["regularMarketDayHigh"]
        ),
        app_icon = "C:/Users/hitma/AppData/Local/Programs/Python/Python310/Python3/Projects/Stock Market Notifier/notif.ico",
        timeout = 15
    )
    time.sleep(60*60*4)