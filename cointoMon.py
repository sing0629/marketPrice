import time
from binance import ThreadedWebsocketManager
from pymongo import MongoClient
from random import randint
from datetime import datetime
import sys
import os

cluster = "mongodb+srv://sing:<passward>@cluster0.u2mpt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
api_key = 'your_api_key'
api_secret = 'your_api_secret'

def main():
    client = MongoClient(cluster)
    db=client.coin
    symbol = 'BTCUSDT'
    symbol2 = 'ETHUSDT'
    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
    # start is required to initialise its internal loop
    twm.start()

    def handle_socket_message(msg):
        pair = msg['data']['s']
        time0 = msg['data']['E']
        price = msg['data']['c']
        filted_str = f'Pair:{pair}, Etime:{time0}, close:{price}'
        # Using dict() + generator expression + split() + map()
        res = dict(map(str.strip, sub.split(':', 1)) for sub in filted_str.split(', ') if ':' in sub)
        print(type(pair),pair,time0, price)
        #filted message is saved to coin.filted full message is saved to coin.full
        result=db.filted.insert_one(res)
        result=db.full.insert_one(msg)

    #start kline socket
    twm.start_kline_socket(callback=handle_socket_message, symbol=symbol)
    twm.start_kline_socket(callback=handle_socket_message, symbol=symbol2)

    # or a multiplex socket can be started like this
    # see Binance docs for stream names
    streams = ['btcusdt@miniTicker','ethusdt@miniTicker']
    twm.start_multiplex_socket(callback=handle_socket_message, streams=streams)

    twm.join()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
       print('Interrupted')
       try:
           sys.exit(0)
       except SystemExit:
           os._exit(0)
           
   #Sample output https://python-binance.readthedocs.io/en/latest/binance.html#binance.client.Client
# {"_id":{"$oid":"620c68f8cad678c26f39c9cb"},
# "e":"kline",                              // Event type
# "E":{"$numberLong":"1644980471814"},      // Event time
# "s":"BTCUSDT",                            // Pair
# "k":                                                  
# 	{"t":{"$numberLong":"1644980460000"},   // Kline start time
# 	"T":{"$numberLong":"1644980519999"},    // Kline close time
# 	"s":"BTCUSDT",                          //Pair
#   "i":"1m",                               // Interval
# 	"f":{"$numberInt":"1258601962"},        // First trade ID
# 	"L":{"$numberInt":"1258602076"},        // Last trade ID
# 	"o":"44057.97000000",                   // Open price
# 	"c":"44052.92000000",                   // Close price
# 	"h":"44057.98000000",                   // High price
# 	"l":"44050.80000000",                   // Low price
# 	"v":"2.94598000",                       // volume
# 	"n":{"$numberInt":"115"},               // Number of trades
# 	"x":false,                              // Is this kline closed?
# 	"q":"129780.54095260",                  // Quote asset volume
# 	"V":"0.58891000",                       // Taker buy volume
# 	"Q":"25944.25576210",                   //Taker buy quote asset volume
# 	"B":"0"}}                               //
