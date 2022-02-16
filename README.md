# marketPrice

Using binance websocket api and get crypto market data then store inside MongoDB

### Change the Configuration 
```
cluster = "mongodb+srv://sing:<passward>@cluster0.u2mpt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
api_key = 'your_api_key'
api_secret = 'your_api_secret'
```
### Getting started
```
pip install python-binance
pip install pymongo
python3 cointoMon.py
```

Sample output https://python-binance.readthedocs.io/en/latest/binance.html#binance.client.Client
```
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
```
MongoDB sample:
```
user_schema = {
    'Pair': {
        'type': 'string',
        'minlength': 1,
        'required': True,
    },
    'Etime': {
        'type': 'int',
        'minlength': 1,
        'required': True,
    },
    'bidV': {
        'type': 'float',
        "required": True,
    },
    'askV': {
        'type': 'float',
        'required': True,
    },
    'bidL': {
        'type': 'string',
        'required': True,
    },
    'askL': {
        'type': 'string',
        'required': True,
    }
}
```
![image](https://user-images.githubusercontent.com/58870660/154257971-88dd612b-47c4-42eb-bac3-8274252ca808.png)

![image](https://user-images.githubusercontent.com/58870660/154258026-20bbcaae-38ce-4729-8262-c286931a7588.png)

