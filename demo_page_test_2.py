# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
#
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(r'C:\Users\m_kow\.wdm\drivers\chromedriver\81.0.4044.69\win32\chromedriver.zip')
#
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')

driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/Test.html')
driver.maximize_window()
driver.find_element_by_id('clickOnMe').click()
driver.switch_to.alert.accept()
driver.find_element_by_id('clickOnMe').click()
driver.switch_to.alert.dismiss()
driver.find_element_by_id('fname').send_keys('Monika')
print('My name is ' + driver.find_element_by_id('fname').get_attribute('value'))
select_element = Select(driver.find_element_by_tag_name('select'))
select_element.select_by_visible_text('Mercedes')
select_element.select_by_value('saab')
select_element.select_by_index(3)
driver.find_element_by_xpath("//input[@type='checkbox']").click()
driver.find_element_by_xpath("//input[@value='female']").click()
print(driver.find_element_by_tag_name('h1').text)
print(driver.find_element_by_id('clickOnMe').text)
print(driver.find_element_by_tag_name('p').get_attribute('textContent')) #ukryty paragraf

print(driver.find_element_by_id('smileImage').size.get('height'))
print(driver.find_element_by_id('smileImage').get_attribute('naturalHeight'))



# driver.find_element_by_name('password').clear()
# driver.find_element_by_name('password').send_keys('hasłooo',Keys.ENTER)
driver.quit()