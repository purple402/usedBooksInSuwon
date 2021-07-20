from bs4 import BeautifulSoup
from selenium import webdriver

def get_last_page(word):
    driver = webdriver.Chrome()
    driver.get("https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=UsedStore&KeyWord=piano&KeyTag=F50+B90")
def get_books(word):
    last_page = get_last_page(word)
    print(last_page)

get_books('python')