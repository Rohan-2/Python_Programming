from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(options=options)

chrome_browser.maximize_window()
chrome_browser.get("https://www.seleniumeasy.com/comment/reply/248#comment-form")

assert "Add new comment " in chrome_browser.title
preview_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
chrome_browser.find_element(By.CSS_SELECTOR, ".btn")
print(preview_button.get_attribute("innerHTML"))

assert "Preview" in chrome_browser.page_source

message = chrome_browser.find_element(By.ID,"edit-name")
message.clear()
message.send_keys("I am Ghost")

message = chrome_browser.find_element(By.ID,"edit-subject")
message.clear()
message.send_keys("Helloo")
preview_button.click()

chrome_browser.close()