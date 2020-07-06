from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')
driver.maximize_window()

driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/Test.html')
username = driver.find_element_by_name('username')

username.clear()

username.send_keys('Monikaaaaaa')