from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#class="a-link-normal"

webpage = requests.get("https://www.boxofficemojo.com/year/2022/")
soup = BeautifulSoup(webpage.content, 'html.parser')
data = soup.find('table')
rows = data.find_all('tr')

#extract column names from table
table_headers = []
for i in data.find_all('th'):
  table_headers.append(i.text)

#extract data from each row 
circ_supply = []
data_table = []
for i in rows:
  table_data = i.find_all('td')
  data = [j.text for j in table_data]
  print(data)
  data_table.append(data)
