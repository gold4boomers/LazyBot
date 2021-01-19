# LazyBot
Real trading bot based on TradingView Alert hooks because I'm lazy.

## The Plan
The plan is simple. Build a micro-service and retire early.

## How will it work
TradingView Alerts support [webhooks](https://www.tradingview.com/support/solutions/43000529348-about-webhooks/). So this bot will be a webserver exposing two basic api calls. Market buy, and Market sell.

## What coins are supported
It will only trade Binance leveraged tokens. If it receives a Sell alert, it will buy the tokenDOWN version. If it receives a Buy alert, it will sell any tokenDOWN held, and buy tokenUP tokens. What can go wrong!
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
The bot market buys a predefined amount of shitcoins calculated in Tether. Load up the account with (total amount of tradeable leveraged token) * predefined bag size in Tether and have fun. 

The maximum amount of bags held at any given time is ~~infinite~~ amount of coins with tradingview alerts configured

There is no maximum drawdown before the bot panic sells


## How do I run this bot
```
docker-compose up -d
```

## I want this or that exchange or this and that function
soon