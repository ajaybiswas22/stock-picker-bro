import pandas

def Datetime_range_stock(df_datetime: pandas.DatetimeIndex, start_date: str, end_date: str) -> pandas.DatetimeIndex:
    """Returns a range of datetime from start date to end date as per df_datetime"""

    if(type(df_datetime.get_loc(start_date)) == slice):
        return df_datetime[df_datetime.get_loc(start_date).start:df_datetime.get_loc(end_date).stop]
    else:
        return df_datetime[df_datetime.get_loc(start_date):df_datetime.get_loc(end_date)+1]

def Datetime_range_close_stock(df_datetime: pandas.DatetimeIndex, start_date: str, end_date: str) -> pandas.DatetimeIndex:
    """Returns a range of datetime (closing time only) from start date to end date as per df_datetime"""
    df_datetime_grouped = df_datetime.groupby(df_datetime.date)
    list_datetime_grouped = list(df_datetime_grouped.values())
    closing_datetime = pandas.DatetimeIndex([x[-1] for x in list_datetime_grouped])
    return Datetime_range_stock(closing_datetime, start_date, end_date)
