import requests
from bs4 import BeautifulSoup

def get_last_page(word):
    response = requests.get("https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=UsedStore&KeyWord=piano&KeyTag=F50+B90")
    soup = BeautifulSoup(response.text, "html.parser")
    pages = soup.select_one('div.Search3_Pager')
    last_page = pages.select_one('div.numbox_last a')
    if last_page == None:
        return 1
    else:
        last_page = last_page.attrs['href']
        last_page = last_page[-4:-2].replace("'", "")
        return int(last_page)


def get_books(word):
    last_page = get_last_page(word)
    print(last_page)

get_books('python')