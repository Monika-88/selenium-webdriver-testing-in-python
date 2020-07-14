from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')
driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/waits.html')
driver.maximize_window()

element_to_click = driver.find_element_by_id('clickOnMe')
element_to_click.click()
time.sleep(5)                                                               #zatrzymujemy wykonywanie programu na 5 sekund
print(driver.find_element_by_tag_name('p').text)
driver.quit()

