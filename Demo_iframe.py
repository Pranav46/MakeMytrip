from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
class demo_iframes():
    def demo_iframe(self):
        fromcity = 'Hubli, India'
        tocity = 'Dubai, United Arab Emirates'
        date = 'Jan 17 2024'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.makemytrip.com/")
        driver.maximize_window()
        time.sleep(10)
        frame = driver.find_element(By.XPATH, "//iframe[@id='webklipper-publisher-widget-container-notification-frame']")
        driver.switch_to.frame(frame)
        driver.find_element(By.XPATH, "//a[@id='webklipper-publisher-widget-container-notification-close-div']").click()
        driver.switch_to.default_content()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='From']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@placeholder='From']").send_keys("hub")
        time.sleep(5)
        driver.find_element(By.XPATH, "//p[contains(.,'" + fromcity + "')]").click()
        time.sleep(5)

        driver.find_element(By.XPATH, "//label[@for='toCity']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@placeholder='To']").send_keys("duba")
        time.sleep(5)
        driver.find_element(By.XPATH, "//p[contains(.,'" + tocity + "')]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[contains(@aria-label, '"+date+"')]").click()
        time.sleep(5)
        driver.save_screenshot("Home.png")
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[normalize-space()='Search']").screenshot("home.png")
        time.sleep(5)

        driver.close()

iframes = demo_iframes()
iframes.demo_iframe()

