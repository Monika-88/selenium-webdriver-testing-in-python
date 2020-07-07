from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')

driver.maximize_window()

driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/Test.html')
hidden_tag= driver.find_element_by_tag_name('p')

if hidden_tag.is_displayed():
    print('Element is displayed')
    print(hidden_tag.text)
else:
    print('Element is not displayed')
    print(hidden_tag.get_attribute('textContent'))

driver.quit()