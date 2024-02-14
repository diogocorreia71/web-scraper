from bs4 import BeautifulSoup
import requests
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

# email
sender_email = "diogo_correia7@hotmail.com"
sender_password = "************"

receiver_email = "diogo_correia7@hotmail.com"

data_file = "scraped_data.json"

# check if data file exists
try:
    with open(data_file, "r") as file:
        existing_data = json.load(file)
except FileNotFoundError:
    existing_data = {}

subject = "Anúncios de hoje"
body = "Resultados: "

# List to store new results
new_results_list = []

# accept multiple makes and models
num_searches = int(input("Quantas pesquisas queres fazer? "))

for _ in range(num_searches):
    marca = input("Qual a marca do carro? ")
    modelo = input("Qual o modelo do carro? ")
    valor = input("Qual o valor máximo? ")
    url = f"https://www.standvirtual.com/carros/{marca}/{modelo}/portocity?search%5Bdist%5D=75&search%5Bfilter_float_price%3Ato%5D={valor}&search%5Border%5D=created_at_first%3Adesc&search%5Bprivate_business%5D=business&search%5Badvanced_search_expanded%5D=true"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    links = doc.find_all(class_="e1oqyyyi9 ooa-1ed90th er34gjf0")
    prices = doc.find_all(class_="e1oqyyyi16 ooa-1n2paoq er34gjf0")
    
	# Append the scraped results to new_results_list
    for link, price in zip(links, prices):
        link_name = link.get_text(strip=True)
        link_href = link.find('a')['href']
        price_text = price.get_text(strip=True)
        new_results_list.append({
            "Marca e modelo": link_name,	
            "Link": link_href,
            "Preço": price_text
		})
        
# Check for new or updated data
new_results = {}
for result in new_results_list:
    key = result["Link"]
    if key not in existing_data or existing_data[key] != result:
        new_results[key] = result

# Send email only if there are new or updated results
if new_results:
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    for result in new_results.values():
        body += f"Marca e modelo: {result['Marca e modelo']}\tLink: {result['Link']}\tPreço: {result['Preço']}\n"
    message.attach(MIMEText(body, "plain"))
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
         server.starttls()
         server.ehlo()
         server.login(sender_email, sender_password)
         server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent succesfully!")
    
	# Update the stored data with the new results
    existing_data.update({result["Link"]: result for result in new_results.values()})
    with open(data_file, "w") as file:
        json.dump(existing_data, file)
    
else:
    print("No new results to send.")