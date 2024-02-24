# Author: Ganesh
# Credit: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import requests
from datetime import datetime as dt
import time

def download():
  url = f"https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1676558075&period2=1708094075&interval=1d&events=history&includeAdjustedClose=true"

  headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

  content = requests.get(url, headers=headers).content
  #print(content)
  return content

def write_file(content):
  """Write input text into a text file"""
  filename = f"MSFT_StockReport_{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.csv"

  with open(filename, 'wb') as file:
    file.write(content)
    return 'success'

def main():
  content = download()
  write_file(content=content)

main()