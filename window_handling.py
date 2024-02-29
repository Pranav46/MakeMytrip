from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as ec

import time
class windoshandling():
    def windows(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.makemytrip.com/")
        driver.maximize_window()
        wait = WebDriverWait(driver,10)
        parentwindow = driver.current_window_handle
        print(parentwindow)
        driver.find_element(By.XPATH, "//span[normalize-space()='Where2Go']").click()
        childwindow = driver.window_handles
        print(childwindow)
        print(len(childwindow))

        for handles in childwindow:
            if handles != parentwindow:
                driver.switch_to.window(handles)
        print(driver.title)
        driver.find_element(By.XPATH, "//a[@href='/tripideas/heritage-destinations']//h3[@class='DestinationCard__CardTitle-sc-1czmno9-1 gMbbQW']").click()
        time.sleep(5)
        driver.close()
        driver.switch_to.window(parentwindow)
        driver.quit()
wh = windoshandling()
wh.windows()
