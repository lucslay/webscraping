from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client

url = 'https://www.livecoinwatch.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

twilio_number = "+12148338562"  
my_number = "+12149573144"
account_SID = "AC09187feaaff69211d80225c786aeb1e9"
token = "de25322108f13840027e967de8d51649"
client = Client(account_SID, token)      
data = soup.findAll("tr", attrs={"class": "table-row filter-row"})

counter1 = 1
counter2 = 1

for row in data:
    cells = row.findAll("td")
    increase_cells = row.findAll("td", attrs={"class":"filter-item table-item item-sort grow change-col"})
    decrease_cells = row.findAll("td", attrs={"class":"filter-item table-item item-sort fall change-col"})
    symbol = cells[counter1].text.split()[0]
    name = cells[counter1].text.split()[1]

    if len(cells[counter1].text.split()) > 2:
        name_holder = ""
        for part_of_name in range(1, len(cells[counter1].text.split())):
            name_holder += cells[counter1].text.split()[part_of_name]
            name_holder += " "
        
        name = name_holder.strip(' ')
    
    currentPrice = cells[counter1 + 1].text
    change24 = cells[counter1 + 7].text
    calcCurrent = float(currentPrice.replace('$',''))

    if symbol == 'BTC' and calcCurrent < 40000:
        BTC_text = client.messages.create(to=my_number, from_=twilio_number, body="Bitcoin is below $40000")
        

    if symbol == 'ETH' and calcCurrent < 3000:
        ETH_text = client.messages.create(to=my_number, from_=twilio_number, body="Ethereum is below $3000")
     
    if counter2 <= 5:
        print(symbol)
        print(name)
        print(calcCurrent)
        if cells[counter1 + 7] in decrease_cells:
            print('Percent of change',change24)
        else:
            print('Percent of change',change24)
        print()
        input()
    
    counter2 += 1