from bs4 import BeautifulSoup
import requests
import csv

my_csv = open('csv_news.csv', 'w')
csv_writer = csv.writer(my_csv)
csv_writer.writerow(['headline', 'news'])

source = requests.get("https://www.vanguardngr.com/").text
soup = BeautifulSoup(source, 'lxml')

latest_news = soup.find('aside')

headline = latest_news.header.text
print(headline.upper())

for news in latest_news.find('ul', id='latest-news-list'):
    news = news.div.text
    print(news)

    print()
    csv_writer.writerow([headline,news])

my_csv.close()
