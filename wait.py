from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')

driver.implicitly_wait(20)
driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/waits2.html')
driver.find_element_by_id('clickOnMe').click()

print(driver.find_element_by_tag_name('p').text)
