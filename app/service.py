from bottle import run, request, post
import os
import logging
import ccxt

os.environ['PYTHONINSPECT'] = 'TRUE'  

logger = logging.getLogger('trader')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('trader.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

try:
    for i in open('./.envrc').read().splitlines():
        k, v = i.split("=")
        os.environ[k]=v
except:
    logging.critical('.envrc missing. Must contain BINANCE_SECRET and BINANCE_API')


def create_session(api: str, secret: str, verbose: bool = False) -> ccxt.Exchange:
        return ccxt.binance({
            'apiKey': api,
            'secret': secret,
            'verbose': verbose,
            })

class RektMachine:

    def __init__(self, session: ccxt.Exchange, bets_size_usdt: float):
        self.session = session
        self.bets_size_usdt = bets_size_usdt

    def bet_balance(self) -> float:
        return self.session.fetch_balance()['USDT']['free']

    def bet_size_as_shitcoin(self, symbol: str = 'BTCUP/USDT') -> float:
        ob = self.session.fetch_order_book(symbol=symbol)
        #calculate with second lowest ask
        #supports total parameter in gui which calculates in usdt
        return self.bets_size_usdt / ob['asks'][1][0]

    def bag_balance(self, coinBase: str = 'SUSHI') -> dict:
        balances = self.session.fetch_balance()
        return  {'UP': balances['total'][f'{coinBase}UP/USDT'],
                'DOWN': balances['total'][f'{coinBase}DOWN/USDT']}

    def bag_dump(self, symbol: str = 'BTCUP/USDT', amount_in_shitcoin: float = 0.0001):
        logging.info(self.session.create_market_sell_order(symbol=symbol, amount=amount_in_shitcoin))

    def bag_pump(self, symbol: str = 'BTCUP/USDT'):
        amount = self.bet_size_as_shitcoin(symbol)
        logging.info(self.session.create_market_buy_order(symbol=symbol, amount=amount))

    def receive_alert(self, coinBase: str = 'BTC', sell: bool = False):
        balances = self.bag_balance(coinBase)
        if sell:
            if balances['UP'] > 0.0:
                self.bag_dump(f'{coinBase}UP/USDT', balances['UP'])
            self.bag_pump(f'{coinBase}DOWN/USDT')
        else:
            if balances['DOWN'] > 0.0:
                self.bag_dump(f'{coinBase}DOWN/USDT', balances['DOWN'])
            self.bag_pump(f'{coinBase}UP/USDT')

@post('/')
def index():
    session_api = create_session(
        api=os.getenv('BINANCE_API'),
        secret=os.getenv('BINANCE_SECRET')
    )
    trader = RektMachine(
        session = session_api,
        bets_size_usdt=20.0
    )
    postdata = request.body.read()
    logger.info(postdata)

    trader.receive_alert(
        coinBase = request.forms.get("name"),
        sell = request.forms.get("sell")
    )
    return "Hi"


run(host='localhost', port=8080, debug=True)