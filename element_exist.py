from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')

driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/Test.html')
driver.maximize_window()

element = driver.find_elements_by_tag_name('br')

if len(element) > 0:
    print('Taki tag istnieje na stronie')
    print(len(element))
else:
    print('Nie znaleziono elementu')

try:
    driver.find_element_by_tag_name('b')
    print('Taki tag istnieje na stronie')
except NoSuchElementException:
    print('Nie znaleziono elementu')

driver.quit()