from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
class demoslider():
    def sliders(self):
        fromcity = 'Mumbai, India'
        tocity = 'Dubai, United Arab Emirates'
        date = 'Jan 27 2024'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.makemytrip.com/")
        wait = WebDriverWait(driver, 20)
        actionchains = ActionChains(driver)
        time.sleep(5)
        #frame = driver.find_element(By.XPATH,"//iframe[@id='webklipper-publisher-widget-container-notification-frame']")
        #driver.switch_to.frame(frame)
        #driver.find_element(By.XPATH, "//a[@id='webklipper-publisher-widget-container-notification-close-div']").click()
        #driver.switch_to.default_content()

        wait.until(ec.presence_of_element_located((By.XPATH, "//span[normalize-space()='From']")))
        driver.find_element(By.XPATH, "//span[normalize-space()='From']").click()

        driver.find_element(By.XPATH, "//input[@placeholder='From']").send_keys("mum")
        wait.until(ec.presence_of_element_located((By.XPATH, "//p[contains(.,'" + fromcity + "')]")))
        driver.find_element(By.XPATH, "//p[contains(.,'" + fromcity + "')]").click()

        driver.find_element(By.XPATH, "//label[@for='toCity']").click()

        driver.find_element(By.XPATH, "//input[@placeholder='To']").send_keys("duba")
        wait.until(ec.presence_of_element_located((By.XPATH, "//p[contains(.,'" + tocity + "')]")))
        driver.find_element(By.XPATH, "//p[contains(.,'" + tocity + "')]").click()

        driver.find_element(By.XPATH, "//div[contains(@aria-label, '" + date + "')]").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Search']").click()
        wait.until(ec.presence_of_element_located((By.XPATH, "(//div[@class='similarPricesCard'])")))
        flights = driver.find_elements(By.XPATH, "(//div[@class='similarPricesCard'])")
        print(len(flights))#to find the number of flights on that day
        time.sleep(10)
        wait.until(ec.presence_of_element_located((By.XPATH, "(//div[@class='rangeslider__handle'])")))
        slider = driver.find_element(By.XPATH, "(//div[@class='rangeslider__handle'])")
        print(slider)
        actionchains.click_and_hold(slider).move_by_offset(-100,0).release().perform()
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "ul[class='appliedFilter'] li")))
        price = driver.find_element(By.CSS_SELECTOR, "ul[class='appliedFilter'] li")
        print(price)
        driver.close()

slider = demoslider()
slider.sliders()