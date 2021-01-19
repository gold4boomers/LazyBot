import os
import logging
import ccxt

os.environ['PYTHONINSPECT'] = 'TRUE'  
try:
    for i in open('./.envrc').read().splitlines():
        k, v = i.split("=")
        os.environ[k]=v
except:
    logging.critical('configuration file not found. create it named .envrc containing BINANCE_SECRET and BINANCE_API')


def tv_alert_symbol(coinBase, sell=False):
    return f'{coinBase}DOWN/USDT' if sell else f'{coinBase}UP/USDT'

def bag_markets():
    exchange = ccxt.binance({
        'apiKey': os.getenv('BINANCE_API'),
        'secret': os.getenv('BINANCE_SECRET'),
        }) 
    markets = [
        coinPair for key,coinPair in exchange.load_markets().items() 
        if any(id in key for id in ['UP/','DOWN/'])
        and coinPair['active']
        ]
    return markets

def bag_balance(coinBase):
    exchange = ccxt.binance({
        'apiKey': os.getenv('BINANCE_API'),
        'secret': os.getenv('BINANCE_SECRET'),
        })
    balances = exchange.fetch_balance()
    return  {'UP': balances[f'{coinBase}UP/USDT']['free'],
             'DOWN': balances[f'{coinBase}DOWN/USDT']['free'],
             'USDT': balances['USDT']}


def bag_dump(symbol, amount_in_shitcoin: float):
        exchange = ccxt.binance({
        'apiKey': os.getenv('BINANCE_API'),
        'secret': os.getenv('BINANCE_SECRET'),
        })
        logging.info(exchange.create_market_sell_order(symbol=symbol, amount=amount_in_shitcoin))

def bag_pump(symbol, amount_in_usdt: float = 10.0):
    exchange = ccxt.binance({
        'apiKey': os.getenv('BINANCE_API'),
        'secret': os.getenv('BINANCE_SECRET'),
    })
    ob = exchange.fetch_order_book(symbol=symbol)
    #calculate with second lowest ask
    #supports total parameter in gui which calculates in usdt
    amount = amount_in_usdt / ob['asks'][1][0]
    logging.info(exchange.create_market_buy_order(symbol=symbol, amount=amount))
