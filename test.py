from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.find_element_by_id('kw').send_keys('haha')
dr.find_element_by_id('su').click()
sleep(3)
dr.close()