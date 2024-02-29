from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as ec

import time
class demo_wait():
    def waits(self):
        fromcity = 'Hubli, India'
        tocity = 'Dubai, United Arab Emirates'
        date = 'Jan 17 2024'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.makemytrip.com/")
        driver.maximize_window()
        #driver.implicitly_wait(10)
        wait = WebDriverWait(driver,5)

        frame = driver.find_element(By.XPATH, "//iframe[@id='webklipper-publisher-widget-container-notification-frame']")
        driver.switch_to.frame(frame)
        driver.find_element(By.XPATH, "//a[@id='webklipper-publisher-widget-container-notification-close-div']").click()
        driver.switch_to.default_content()
        wait.until(ec.presence_of_element_located((By.XPATH, "//span[normalize-space()='From']")))
        driver.find_element(By.XPATH, "//span[normalize-space()='From']").click()

        driver.find_element(By.XPATH, "//input[@placeholder='From']").send_keys("hub")
        wait.until(ec.presence_of_element_located((By.XPATH, "//p[contains(.,'" + fromcity + "')]")))
        driver.find_element(By.XPATH, "//p[contains(.,'" + fromcity + "')]").click()


        driver.find_element(By.XPATH, "//label[@for='toCity']").click()

        driver.find_element(By.XPATH, "//input[@placeholder='To']").send_keys("duba")
        wait.until(ec.presence_of_element_located((By.XPATH, "//p[contains(.,'" + tocity + "')]")))
        driver.find_element(By.XPATH, "//p[contains(.,'" + tocity + "')]").click()

        driver.find_element(By.XPATH, "//div[contains(@aria-label, '"+date+"')]").click()

        driver.save_screenshot("Home.png")

        driver.find_element(By.XPATH, "//a[normalize-space()='Search']").screenshot("home.png")


        driver.close()

wait =demo_wait ()
wait.waits()

