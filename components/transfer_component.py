import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Transfer:
    PATH = '/html/body/main/section/nav/button[3]'

    def __init__(self, driver):
        self.driver = driver

    def transfers(self):
        transfers_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/nav/button[3]')))
        transfers_button.click()

    def search_transfer_market(self):
        search_transfer_market = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[2]')))

        while True:
            try:
                search_transfer_market.click()
                break
            except Exception as e:
                time.sleep(1)
