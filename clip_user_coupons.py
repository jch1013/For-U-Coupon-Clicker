from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def clip_coupons(username, password):
    driver = webdriver.Chrome("chromedriver")
