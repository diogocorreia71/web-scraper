from bs4 import BeautifulSoup
import requests
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

marca = input("Qual a marca do carro? ")
modelo = input("Qual o modelo do carro? ")
valor = input("Qual o valor máximo? ")

#Stand Virtual parser
url = f"https://www.standvirtual.com/carros/{marca}/{modelo}?search%5Bfilter_float_price%3Ato%5D={valor}&search%5Border%5D=created_at_first%3Adesc&search[private_business]=business&search[advanced_search_expanded]=true"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

links = doc.find_all(class_="e1oqyyyi9 ooa-1ed90th er34gjf0")
prices = doc.find_all(class_="e1oqyyyi16 ooa-1n2paoq er34gjf0")

#email
sender_email = "diogo_correia7@hotmail.com"
sender_password = "*************"

receiver_email = "diogo_correia7@hotmail.com"

subject = "Anúncios de hoje"
body = "Resultados"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

for link, price in zip(links, prices):
    link_name = link.get_text(strip=True)
    link_href = link.find('a')['href']
    price_text = price.get_text(strip=True)
    body += f"Marca e Modelo: {link_name}\tLink: {link_href}\tPreço: {price_text}\n"
    
message.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    
print("Email sent succesfully!")