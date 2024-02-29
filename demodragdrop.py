from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


import time

class demodragsdrop():
    def dragdrop(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demoqa.com/droppable")
        driver.maximize_window()
        time.sleep(5)
        actionchains = ActionChains(driver) #instance of action chain
        source = driver.find_element(By.ID, "draggable")
        destination = driver.find_element(By.XPATH, "(//div[@id='droppable'])[1]")
        actionchains.drag_and_drop(source, destination).perform()
        actionchains.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform() #shorcutkeys
        time.sleep(5)
        driver.close()
dragd = demodragsdrop()
dragd.dragdrop()