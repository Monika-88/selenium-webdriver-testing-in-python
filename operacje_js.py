from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')

driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/Test.html')
driver.maximize_window()

driver.execute_script('arguments[0].click();',driver.find_element_by_id("newPage"))

wartosc = 'Monika'
driver.execute_script("arguments[0].setAttribute('value', '" + wartosc + "')", driver.find_element_by_id('fname'))


#gdy metody .click i .sendKeys nie zadzialaja mozna posilkowac sie java script jak wyzej