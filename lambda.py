from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')
wait = WebDriverWait(driver,10,0.5)
driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/waits2.html')
driver.find_element_by_id('clickOnMe').click()
wait.until(lambda wd: len(wd.find_element_by_tag_name("p")) == 1)
print(driver.find_element_by_tag_name('p').text)


driver.quit()