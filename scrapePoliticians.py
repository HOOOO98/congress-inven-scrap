from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://policy.nec.go.kr/')
driver.implicitly_wait(10)

menulink = driver.find_element(By.CSS_SELECTOR, '#header div.sgList a:nth-child(3)')

menulink.click()
