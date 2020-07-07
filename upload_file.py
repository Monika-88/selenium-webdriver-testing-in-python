from selenium import webdriver
import os                             #pobieranie pliku

driver = webdriver.Chrome(r'C:\Users\m_kow\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe')

driver.get('file:///C:/Users/m_kow/OneDrive/Documents/kurs%20selenium/FileUpload.html')

upload_input = driver.find_element_by_id('myFile')
path = os.path.abspath('upload.txt')  #pobieranie pliku

driver.save_screenshot('screenshots/before_upload.jpg')

upload_input.send_keys(path)

driver.save_screenshot('screenshots/after_upload.jpg')        #zrzut ekranu

driver.quit()