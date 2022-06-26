import pandas
from resources.datetimeutil import datetimemgr

def profit(old_price: float, new_price: float) -> float:
    return new_price-old_price

def profit_percent(old_price: float, new_price: float) -> float:
    return ((new_price-old_price)*100.0)/old_price

def profit_percent_stock(df_sheet: pandas.core.frame.DataFrame, stock_ticker: str, start_date: str, end_date: str) -> float:
    """Finds profit percentage of a stock from start_date closing to end_date closing"""
    dates = df_sheet.index # DateTimeIndex
    dates_range = datetimemgr.Datetime_range_close_stock(dates, start_date, end_date)  # DateTimeIndex
    prices = df_sheet.loc[dates_range][stock_ticker]  # series
    return profit_percent(prices['Close'].iloc[0], prices['Close'].iloc[-1]) # diff. b/w first and last day
