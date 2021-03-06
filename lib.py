from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

def make_driver(word, lib):
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://www.suwonlib.go.kr:8443/')
    select = Select(driver.find_element_by_class_name('select-all'))
    select.select_by_value(lib)
    elem_search = driver.find_element_by_xpath('//*[@id="search"]')
    elem_search.send_keys(word)
    driver.find_element_by_xpath('//*[@id="nav"]/div[1]/div[2]/div/div/button[2]').click()
    return driver

def get_last_page(driver):
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    total = soup.select_one('#srch_category > div > div.srch_info > span.highlight').text
    total = total.replace('\xa0', '').replace(',', '')
    total = int(total)
    if total == 0:
        return 0
    elif total % 10 == 0:
        return total // 10
    else:
        return (total // 10) + 1

def get_books_info(driver):
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.select_one('div.resutl_list2').select('div.book_list2')
    book_info = []
    for book in books:
        image = book.select_one('div.book_img_wrap img')['src']
        title = book.select_one('div.top_title > h1 > span').text
        lib = book.select_one('div.book_contents_wrap > div.contents_wrap_top > div > ul:nth-child(3) > span:nth-child(1)').text
        state = book.select_one('div.top_title > ul:nth-child(4) > span').text.lstrip().replace('\n               ', ' ')
        book_info.append({"image": image, "title": title, "lib" : lib, "state": state})
    return book_info

def extract_books(driver, last_page):
    if last_page == 0:
        driver.close()
        return []
    books = get_books_info(driver)
    for i in range(2, last_page + 1):
        print(f"scrapping lib page {i}")
        driver.find_element_by_xpath(f'//*[@id="wrap"]/div[2]/div[3]/input[{i + 2}]').click()
        books.extend(get_books_info(driver))
    driver.close()
    return books

def get_books(word, lib):
    driver = make_driver(word, lib)
    last_page = get_last_page(driver)
    books = extract_books(driver, last_page)
    return books