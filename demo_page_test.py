from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/Test.html')
driver.maximize_window()
driver.find_element(By.ID,'newPage')
driver.find_element_by_id('newPage').click()
driver.find_element_by_link_text('Visit W3Schools.com!')
driver.find_elements_by_partial_link_text('Visit W3Schools.c')
driver.find_element_by_class_name('topSecret')
driver.find_element_by_xpath("html/body/table/tbody/tr/th")
driver.find_element_by_xpath("//tbody//th")
driver.find_element_by_xpath("//th")
driver.find_element_by_xpath("//th[text()='Month']")
driver.find_element_by_xpath('/html/body/a[1]')

elements_list_length = len(driver.find_elements_by_xpath("//th"))
print(elements_list_length)

driver.quit()

#driver.close()