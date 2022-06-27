import pandas
from  pandas.core.frame import DataFrame
import numpy
from resources.datetimeutil import datetimemgr

def profit(old_price: float, new_price: float) -> float:
    return new_price-old_price

def profit_percent(old_price: float, new_price: float) -> float:
    return ((new_price-old_price)*100.0)/old_price

def profit_percent_stocks(df_sheet: DataFrame, 
                          stock_tickers: list, feature_names: list, 
                          start_date: str, end_date: str) -> DataFrame:
    """Finds profit percentage of a stock based on feature 
    from start_date (investment day) closing to end_date closing"""
    dates = df_sheet.index # DateTimeIndex
    dates_range = datetimemgr.Datetime_range_close_stock(dates, start_date, end_date)  # DateTimeIndex
    prices_tickers = [df_sheet.loc[dates_range][stock_ticker] for stock_ticker in stock_tickers]   # series
    # percent diff. b/w first and last day
    percentages = [profit_percent(prices[feature_names].iloc[0], prices[feature_names].iloc[-1]) 
                                   for prices in prices_tickers]
    df_percentages = pandas.DataFrame(percentages, columns=feature_names, dtype=float, index=stock_tickers)
    return df_percentages

def profit_percent_avg_stocks(df_sheet: DataFrame, 
                              stock_tickers: list, feature_names: list, start_date: str, end_date: str) -> DataFrame:
    """Finds average profit percentage of a stock based on feature
    from start_date closing (investment day) to end_date closing"""
    dates = df_sheet.index  # DateTimeIndex
    dates_range = datetimemgr.Datetime_range_close_stock(dates, start_date, end_date)  # DateTimeIndex
    prices_tickers = [df_sheet.loc[dates_range][stock_ticker] for stock_ticker in stock_tickers]   # series
    # percent diff. b/w first and all days
    average_percentages = []
    for prices in prices_tickers:
        percentages = []
        for i in range(1,len(prices[feature_names])):
            percentages.append(profit_percent(prices[feature_names].iloc[0], prices[feature_names].iloc[i]))
        average_percentages.append(numpy.array(percentages).mean(0))
    df_average_percentages = pandas.DataFrame(average_percentages, columns=feature_names, dtype=float, index=stock_tickers)
    return df_average_percentages

def best_stocks(df_sheet: DataFrame,
                stock_tickers: list, feature_names: list, 
                start_date: str, end_date: str,
                amount: int, to_average: bool = False,
                worst: bool = False) -> DataFrame:
    """Returns best stocks while considering percentage returns of the features provided"""
    if(to_average == True):
        df = profit_percent_avg_stocks(df_sheet,stock_tickers,feature_names,start_date,end_date)
    else:
        df = profit_percent_stocks(df_sheet, stock_tickers, feature_names, start_date, end_date)
    return df.sort_values(by=feature_names,ascending=worst).head(amount)
