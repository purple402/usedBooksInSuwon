from selenium import webdriver
from selenium.webdriver.support.ui import Select
def make_driver(word):
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://www.suwonlib.go.kr:8443/')
    select = Select(driver.find_element_by_class_name('select-all'))
    select.select_by_value('SB')
    elem_search = driver.find_element_by_xpath('//*[@id="search"]')
    elem_search.send_keys(word)
    driver.find_element_by_xpath('//*[@id="nav"]/div[1]/div[2]/div/div/button[2]').click()
    return driver

def get_books(word):
    driver = make_driver(word)
