# Author: Ganesh
# Credit: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import requests
from datetime import datetime as dt
import time

def get_news(topic, from_date, to_date, language):
  #url = f"https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-01-18&to=2024-2-17&sortBy=popularity&language=en&apiKey=c7dd69570203420d9aeddfcbd74b016b"
  url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey=c7dd69570203420d9aeddfcbd74b016b"
  #headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

  r = requests.get(url)
  #print(content)
  content = r.json()
  print(content)
  print(type(content))
  articles = content['articles']
  print(type(articles))
  #contentAuthor = content['articles'][0]['author']
  #contentDESC = content['articles'][0]['description']
  #print(contentDESC)
  #print(F'Author: {contentAuthor}  Desc: {contentDESC}'  )
  
  #create for each loop on articles
  i = 0
  for article in articles:
    contentArticle = article['title']
    contentDESC = article['description']
    i+=1
    print(F'{i}, Title: {contentArticle}  \n Desc: {contentDESC} \n'  )
  
  #return content

def main():
  #content = download()
  get_news('stock%20market',from_date='2024-01-18',to_date='2024-02-18',language='en')

main()