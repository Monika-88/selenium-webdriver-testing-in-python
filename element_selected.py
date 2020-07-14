from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')
driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/Test.html')
driver.maximize_window()

checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")

if checkbox.is_selected():
    print('Element jest zaznaczony. Odznaczam!')
    checkbox.click()
else:
    print('Element nie jest zaznaczony. Zaznaczam!')
    checkbox.click()

driver.save_screenshot('screenshots\element_selected.jpg')
driver.quit()