from bs4 import BeautifulSoup
import requests

src = requests.get(
    "https://www.newegg.com/Black-Friday-Sale/EventSaleStore/ID-42").text
items = []
soup = BeautifulSoup(src, 'lxml')
anchors = soup.find_all("a", {"class": "item-title"})
for anchor in anchors:
    items.append(anchor.get_text())

price_html = soup.find_all("li", {"class": "price-current"})
prices = []
for price in price_html:
    price = price.get_text()
    s_idx = price.index("$") + 1
    end_idx = price.index(".") + 3
    num = price[s_idx:end_idx]
    num = num.replace(",", "")
    prices.append(float(num))

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
item_obj = []

for i in range(len(prices)):
    to_append = Item(items[i], prices[i])
    item_obj.append(to_append)

for item in item_obj:
    print(f"Name: {item.name}")
    print(f"Price: {item.price}\n")


