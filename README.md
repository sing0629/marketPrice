# marketPrice

Using binance websocket api and get crypto market data then store inside MongoDB

### Getting started

```
pip install python-binance
pip install pymongo
python3 cointoMon.py
```

Sample output https://python-binance.readthedocs.io/en/latest/binance.html#binance.client.Client

{"\_id":{"$oid":"620c68f8cad678c26f39c9cb"},
"e":"kline",                              // Event type
"E":{"$numberLong":"1644980471814"}, // Event time
"s":"BTCUSDT", // Pair
"k":  
 {"t":{"$numberLong":"1644980460000"},   // Kline start time
	"T":{"$numberLong":"1644980519999"}, // Kline close time
"s":"BTCUSDT", //Pair
"i":"1m", // Interval
"f":{"$numberInt":"1258601962"},        // First trade ID
	"L":{"$numberInt":"1258602076"}, // Last trade ID
"o":"44057.97000000", // Open price
"c":"44052.92000000", // Close price
"h":"44057.98000000", // High price
"l":"44050.80000000", // Low price
"v":"2.94598000", // volume
"n":{"$numberInt":"115"}, // Number of trades
"x":false, // Is this kline closed?
"q":"129780.54095260", // Quote asset volume
"V":"0.58891000", // Taker buy volume
"Q":"25944.25576210", //Taker buy quote asset volume
"B":"0"}} //
