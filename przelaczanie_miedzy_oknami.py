# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
#
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')

driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/Test.html')
driver.maximize_window()

driver.find_element_by_id('newPage').click()
print(driver.title)

current_window_name = driver.current_window_handle
window_names = driver.window_handles

for window in window_names:
    if window != window_names:
        driver.switch_to.window(window)

print(driver.title)

driver.switch_to.window(current_window_name)

print(driver.title)







driver.quit()