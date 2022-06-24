def profit(old_price: float, new_price: float):
    return new_price-old_price

def profit_percent(old_price: float, new_price: float):
    return ((new_price-old_price)*100.0)/old_price
