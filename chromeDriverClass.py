from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

class chromeDriverClass():

    def __init__(self, url):
        self.option = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=self.option)
        self.browser.get(url)
        self.browser.maximize_window()

    def getPageSearch(self, position):

        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR, '.q').send_keys(position)
        self.browser.find_element(By.CSS_SELECTOR, '.btn1').click()

        try:
            position = self.browser.find_element(By.CSS_SELECTOR, '.col-sm-4')
            link = position.find_element(By.CSS_SELECTOR, '.item > .title > a')
            self.browser.find_element(By.CSS_SELECTOR, '.q').clear()

            return link.get_attribute('href')
        except NoSuchElementException:
            self.browser.find_element(By.CSS_SELECTOR, '.q').clear()

            return ('LinkIsNotFind')







