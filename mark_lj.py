
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://mark--mywords.livejournal.com/")
data  = driver.find_elements_by_css_selector ("tbody > tr > td > table.s2-entrytext > tbody > tr > td:not(.comments)")

for datum in data: 
    print datum.text

driver.close()
