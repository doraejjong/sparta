from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

driver = webdriver.Chrome('/Users/John/Desktop/sparta/test/chromedriver', options=options)
driver.get('https://store.naver.com/restaurants/list?bounds=127.0983469%3B37.3923675%3B127.1240103%3B37.4045388&filterId=s20543619&query=%ED%8C%90%EA%B5%90%EC%97%AD%20%EB%A7%9B%EC%A7%91&sessionid=DXh8oq%2FHmrvdZ35b0zc6jQ%3D%3D');
# sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

driver.find_element_by_xpath('//*[@id="_business_36276299"]/div/div/div[1]/span/a/span').click()


