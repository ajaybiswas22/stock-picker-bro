import yfinance as yf

def print_info(yf_tickers):
    if isinstance(yf_tickers, yf.Ticker):
        print(f"\n{'='*80}")
        space = ' '
        print(f"{space*33}{yf_tickers.info['symbol']}\n")
        for key in yf_tickers.info:
            print(f"--> {key:>29} : {yf_tickers.info[key]}")

    elif isinstance(yf_tickers, yf.Tickers):
        for ticker in yf_tickers.tickers:
            print(f"\n{'='*80}")
            space = ' '
            print(f"{space*33}{ticker.info['symbol']}\n")
            for key in ticker.info.keys():
                print(f"--> {key:>29} : {ticker.info[key]}")


def print_table(yf_tickers):
    if isinstance(yf_tickers, yf.Ticker):
        ticker = yf_tickers
        print(f"| {ticker.info.get('symbol','NONE'):<5} | {ticker.info.get('sector','NONE'):>25} | " +
              f"{ticker.info.get('currency','NONE'):>4} | {ticker.info.get('quoteType','NONE'):>6} | " +
              f"{ticker.info.get('shortName','NONE'):<35} |")

    elif isinstance(yf_tickers, yf.Tickers):
        for ticker in yf_tickers.tickers:
            print(f"| {ticker.info.get('symbol','NONE'):<5} | {ticker.info.get('sector','NONE'):>25} | " +
                  f"{ticker.info.get('currency','NONE'):>4} | {ticker.info.get('quoteType','NONE'):>6} | " +
                  f"{ticker.info.get('shortName','NONE'):<35} |")
