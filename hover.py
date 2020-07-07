from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')

driver.get('https://www.w3schools.com/')
driver.maximize_window()

web_element = driver.find_element_by_id('navbtn_references')
webdriver.ActionChains(driver).move_to_element(web_element).click().perform()