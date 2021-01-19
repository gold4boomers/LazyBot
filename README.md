# LazyBot
Real trading bot based on TradingView Alert hooks because I'm lazy.


## The Plan
The plan is simple. Build a micro-service and retire early.

## How will it work

TradingView Alerts support [webhooks](https://www.tradingview.com/support/solutions/43000529348-about-webhooks/). So this bot will be a webserver exposing two basic api calls. Market buy, and Market sell.

## What coins are supported
It will only trade Binance leveraged tokens. If it receives a Sell alert, it will buy the tokens DOWN version. If it receives a Buy alert, it will sell any DOWN tokens if held, and buy UP tokens. What can go wrong!
- GRT
- XLM
- SUSHI
- AAVE
- YFI
- FIL
- SXP
- UNI
- LTC
- XRP
- DOT
- TRX
- EOS
- XTZ
- BNB
- LINK
- ADA
- ETH
- BTC


## How will it lose my money
The bot market buys a predefined amount of shitcoins calculated in Tether. Load up the account with 20 times the predefined bag size in Tether. 

The maximum amount of bags held at a given time is 5. 

The maximum drawdown before the bot panic sells is 33%.


## How do I run this bot
```
docker-compose up -d
```