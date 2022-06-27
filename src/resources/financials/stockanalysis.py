from resources.datetimeutil import datetimemgr
import pandas
from pandas.core.frame import DataFrame
from pandas.core.series import Series


def stock_history(df_sheet: DataFrame, stock_ticker: str, feature_name: str, 
                  start_date: str, end_date: str, display: bool = False) -> Series:
    """Returns historical data (start_date to end_date) of a stock based on a feature"""
    dates = df_sheet.index  # DateTimeIndex
    dates_range = datetimemgr.Datetime_range_close_stock(dates, start_date, end_date)  # DateTimeIndex
    data = df_sheet.loc[dates_range][stock_ticker][feature_name]  # series
    if(display == True):
        data.plot()
    return data
