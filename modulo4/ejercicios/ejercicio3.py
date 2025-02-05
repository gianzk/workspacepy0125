from bs4 import BeautifulSoup
import requests
url="https://pokeapi.co/"
response=requests.get(url)

data=response.text
soup = BeautifulSoup(data, 'html.parser')
divs=soup.find_all('div')
#print(soup.prettify())
print(type(divs))