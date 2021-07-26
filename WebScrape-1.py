import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/redmi-9i-midnight-black-64-gb/p/itm0e1018dac2627?pid=MOBFV8RYKWQ3HACE&lid=LSTMOBFV8RYKWQ3HACEV2QOWQ&marketplace=FLIPKART&q=phone&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_HistoryAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_5_na_na_na&fm=SEARCH&iid=035f7fcf-d060-4624-89a8-4b9a840594f9.MOBFV8RYKWQ3HACE.SEARCH&ppt=hp&ppn=homepage&ssid=m999q5yyds0000001623951702378&qH=f7a42fe7211f98ac'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all("li", class_="_16eBzU col")
# quotes = soup.find_all("span", class_="u8dYXW")
quotes = soup.find_all("span", class_="fGhUR2")
# print(quotes)

for q in quotes:
    print(q.text)
