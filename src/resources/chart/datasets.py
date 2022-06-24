import datetime
from bs4 import BeautifulSoup as bs
import requests

def get_snp500_tickers_from_wiki():
    "returns list of tuples to add to my sql. IT downloads and parses list of S&P 500 companies from Wikipedia"
    now = datetime.datetime.utcnow()
    
    response = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    
    soup = bs(response.text,features='lxml')
    
    symbol_list = soup.select('table')[0].select('tr')[1:]
    
    symbols = []
    for i, symbol in enumerate(symbol_list):
        tds = symbol.select('td')
        symbols.append(tds[0].select('a')[0].text)   #this adds just the ticker
        
        #uncomment the section below and comment out the append above if you want to 
        #return a tuple with more information. 
#         symbols.append(
#             (
#                 tds[0].select('a')[0].text,  #ticker
#                 'stock',
#                 tds[1].select('a')[0].text,  #name
#                 tds[3].text,   #sector
#                 'USD', now, now
#             )
#         )
    
    return symbols