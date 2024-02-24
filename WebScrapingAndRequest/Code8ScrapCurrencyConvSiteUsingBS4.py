#Author: Ganesh

from bs4 import BeautifulSoup
import requests

def get_Currency(in_currency, out_currency,amount):
    url=f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amount}"
    content = requests.get(url).text
    #print(content)
    soup = BeautifulSoup(content,'html.parser')
    #rate = soup.find("span",class_="ccOutputRslt")
    rate = soup.find("span",class_="ccOutputRslt").getText()
    #print(rate)
    #to print only number
    currency = rate[-3:]
    rate = rate[:-4]
    #convert rate to float
    rate = float(rate)
    print(f'Exchange rate is {rate} in currency {currency}')
    
get_Currency(in_currency='KWD',out_currency='INR',amount=1)