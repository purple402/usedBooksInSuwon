import requests
from bs4 import BeautifulSoup
def get_books(word):
    last_page = get_last_page(word)
    print(last_page)

get_books('python')