import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1900,1900)
driver.get('https://docs.google.com/spreadsheets/d/12-P5XcVUfZ-jeSKt8btAgNNc7tEbf7oOJIqPA_9gwI4/edit#gid=1715037745')
time.sleep(10)
screen = driver.save_screenshot('screen.png')
driver.quit()