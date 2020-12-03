#BTC PRICE IN REAL TIME FROM GOOGLE SEARCH

from bs4 import BeautifulSoup
import requests
import time

#Get the URL
url = 'https://www.google.com/search?q=preco+bitcoin&oq=preco+bitecoin&aqs=chrome..69i57j0l7.3753j1j7&sourceid=chrome&ie=UTF-8'

#Make a request to the website
HTML = requests.get(url)

#Parse the HTML
soup = BeautifulSoup(HTML.text, 'html.parser')

#Print doup to find where the texgt is that contains the price of the cryptocurrency 
#print(soup.prettify())

#<div class="BNeawe iBp4i AP7Wnd">

#Create a function to get the price of a cryptocurrency 
def get_crypto_price(coin):
  #Get the URL for example
  url = 'https://www.google.com/search?q=preco+bitcoin&oq=preco+bitecoin&aqs=chrome..69i57j0l7.3753j1j7&sourceid=chrome&ie=UTF-8'

  #Make a request to the website
  HTML = requests.get(url)

  #Parse the HTML
  soup = BeautifulSoup(HTML.text, 'html.parser')

  #Find the current price
  text = soup.find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).text

  #Return the text
  return text

#Get the price of a cryptocurrency
price = get_crypto_price('BTC')

#Print the price
#print(price)

#Create a function to consistently show the price of the cryptocurrency when it changes
def main():
  last_price = -1
  # Create a loop to continuously show the price
  while True:
    #Choose the cryptocurrency that i want to get the price for
    crypto = 'BTC'
    #Get the price of the cryptocurrency
    price = get_crypto_price(crypto)
    #Check if the price changed
    if price != last_price:
      print('1',crypto+' price: ', price)
      last_price = price
    time.sleep(3)

#Run/Execute the main function
main()
