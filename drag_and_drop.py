from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')

def wait_until_not_visible(element):
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.invisibility_of_element(element))

driver.get('https://demos.telerik.com/kendo-ui/dragdrop/index')
driver.maximize_window()
draggable = driver.find_element_by_id('draggable')
droptarget = driver.find_element_by_id('droptarget')

accept_cookies_button = driver.find_element_by_xpath("//button[text()='Accept Cookies']")
accept_cookies_button.click()
wait_until_not_visible(accept_cookies_button)
webdriver.ActionChains(driver).drag_and_drop(draggable,droptarget).perform()