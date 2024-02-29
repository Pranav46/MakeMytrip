from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


import time

class demoactions():
    def demoaction(self):
        fromcity = 'Hubli'
        tocity = 'Dubai, United Arab Emirates'
        date = 'Jan 17 2024'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        time.sleep(10)
        driver.get("https://www.makemytrip.com/")
        time.sleep(10)
        #frame = driver.find_element(By.XPATH,"//iframe[@id='webklipper-publisher-widget-container-notification-frame']")
        #driver.switch_to.frame(frame)
        #driver.find_element(By.XPATH, "//a[@id='webklipper-publisher-widget-container-notification-close-div']").click()
        #driver.switch_to.default_content()
        actionchains =ActionChains(driver) #same for all code
        time.sleep(5)
        #rightclick in mouse
        #actionchains.context_click().perform()
        #search = driver.find_element(By.XPATH, "//a[normalize-space()='Search']")
        #actionchains.context_click(search).perform()
        # mouse movement
        #element = driver.find_element(By.XPATH, "//span[normalize-space()='From']")
        #actionchains.move_to_element(element).perform()
        #actionchains.click().perform() #this click is for actionchain
        time.sleep(10)

        driver.close()
actions = demoactions()
actions.demoaction()
