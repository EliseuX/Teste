from tkinter import Scrollbar
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.tiobe.com/tiobe-index/')
time.sleep(3)
driver.execute_script('window.scrollTo(84,677)')
time.sleep(2)
text = driver.find_element(By.XPATH, '//*[@id="top20"]/tbody/tr[1]/td[5]').text
print('Top 1:',text)

driver.close()




