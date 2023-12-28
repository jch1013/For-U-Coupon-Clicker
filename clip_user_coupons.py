from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait

def clip_coupons(username, password):

    # set up chrome webdriver and get the login page to the for u coupons
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.safeway.com/foru/coupons-deals.html")

    # login to for u website
    WebDriverWait(driver, 5000)

    driver.find_element("id", "label-email").send_keys(username)
    driver.find_element("id", "label-password").send_keys(password)
    driver.find_element("id", "btnSignIn").send_keys(Keys.ENTER)

    WebDriverWait(driver, 5000)
    print(driver.page_source)


    # get all coupons from webpage
    coupons = driver.find_elements("class name", "grid-coupon-click-button")
    for coupon in coupons:
        print(coupon)
    print("number of coupons: " + str(len(coupons)))
