from bs4 import BeautifulSoup
import requests
import re

marca = input("Qual a marca do carro? ")
modelo = input("Qual o modelo do carro? ")
valor = input("Qual o valor máximo? ")

url = f"https://www.standvirtual.com/carros/{marca}/{modelo}?search%5Bfilter_float_price%3Ato%5D={valor}&search%5Border%5D=created_at_first%3Adesc&search[private_business]=business&search[advanced_search_expanded]=true"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

links = doc.find_all(class_="e1oqyyyi9 ooa-1ed90th er34gjf0")
prices = doc.find_all(class_="e1oqyyyi16 ooa-1n2paoq er34gjf0")

for link, price in zip(links, prices):
    link_name = link.get_text(strip=True)
    link_href = link.find('a')['href']
    price_text = price.get_text(strip=True)
    print(f"Marca e Modelo: {link_name}\tLink: {link_href}\tPreço: {price_text}\n")