from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://books.toscrape.com/").text

soup = BeautifulSoup(source, "lxml")

csv_file = open("book_scraper.csv", "w")
csv_writer = csv.writer(csv_file)

csv_writer.writerow(["title", "cost", "availability"])

for article in soup.find_all("article"):
    book_title = article.h3.a["title"].strip()
    book_cost = article.find("p", class_="price_color").text.strip()
    book_available = article.find("div", class_="product_price").find("p", class_="instock availability").text.strip()

    print(book_title)
    print(book_cost)
    print(book_available)
    print()

    csv_writer.writerow([book_title, book_cost, book_available])


csv_file.close()



