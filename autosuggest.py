from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
class autos():
    def auto(self):
        fromcity = 'Hubli, India'
        tocity = 'Dubai, United Arab Emirates'
        date = 'Jan 17 2024'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.makemytrip.com/")
        time.sleep(5)
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

at = autos()
at.auto()
