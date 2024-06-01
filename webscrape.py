import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

file = open("scraped_quotes.csv","w")
writer = csv.writer(file)

writer.writerow(["QUOTES","AUTHORS"])

for quote , author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])
file.close()
