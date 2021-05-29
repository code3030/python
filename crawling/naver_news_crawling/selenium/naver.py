from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import datetime
import os, sys

chromdrive_url = "c://projects/crawling/selenium/chromedriver.exe"
url = "https://news.naver.com/main/list.nhn"

if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path)
else:
    driver = webdriver.Chrome(chromdrive_url)

driver.get(url)
driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[2]/div/div[2]/div/div/a[2]").click()
soup = bs(driver.page_source, 'html.parser')
soup = soup.find(class_='list_body')
rows = soup.find_all('li')

news = []

for row in rows:
    # article_title = row.get_text().strip()
    # news.append(article_title)

    article_title = row.find('a', class_="nclicks(fls.list)")
    article_title = article_title.get_text().strip()
    
    article_writing = row.find('span', class_="writing")
    article_writing = article_writing.get_text().strip()
    
    article_date = row.find('span', class_="date")
    article_date = article_date.get_text().strip()
    
    news.append(article_title + '(' + article_writing + ' / ' + article_date + ')')

str_news = "\n".join(news)

now = datetime.datetime.now()
nowDatetime = now.strftime('%y%m%d-%H%M%S')
storage = ".\\N_News_" + nowDatetime + '.txt'

f = open(storage, "w", encoding='utf-8')
f.write(str_news)
f.close

driver.close()