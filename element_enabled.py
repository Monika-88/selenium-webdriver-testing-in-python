from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')

driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/Test.html')
driver.maximize_window()

first_name_input = driver.find_element_by_name('fname')

if first_name_input.is_enabled():
    first_name_input.send_keys('Monika')


else: print('Nie mozemy wpisac tekstu')

# if first_name_input.is_displayed():                 # wpisane displayed a nie disabled :)
#     print('Nie mozemy wpisac tekstu')
#
#
# else: first_name_input.send_keys('Monika')