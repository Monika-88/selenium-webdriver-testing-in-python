from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')

driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/IFrameTest.html')
driver.maximize_window()

print(driver.find_element_by_tag_name('h1').text)
driver.switch_to.frame(driver.find_element_by_tag_name('iframe')) #przeniesienie do ramki
print(driver.find_element_by_tag_name('h1').text)
driver.switch_to.default_content()                  #przeniesienie do strony domyślnej
print(driver.find_element_by_tag_name('h1').text)

driver.quit()