from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')

driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/DoubleClick.html.html')
driver.maximize_window()
button = driver.find_element_by_id('bottom')

# webdriver.ActionChains(driver).double_click(button).perform()   #podwójne kliknięcie

webdriver.ActionChains(driver).context_click(button).perform()  # kliknięcie prawym przyciskiem myszy
