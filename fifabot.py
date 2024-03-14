from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.utils import get_security_code
from utils.credentials import email, pasword, email_password
from components.transfer_component import Transfer

PATH = "https://www.ea.com/tr-tr/ea-sports-fc/ultimate-team/web-app/"


class FifaBot:

    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)  # Initialize the driver instance
        self.driver.get(PATH)
        self.log_in()

        self.transfer = Transfer(self.driver)

    def log_in(self):
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Login"]/div/div/button[1]')))
        login_button.click()

        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
        email_input.send_keys(email)

        passwrd_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        passwrd_input.send_keys(pasword)

        signin_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="logInBtn"]')))
        signin_button.click()

        send_code_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="btnSendCode"]')))
        send_code_button.click()

        code_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="twoFactorCode"]')))
        code_input.send_keys(get_security_code(email, email_password))

        submit_code_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="btnSubmit"]')))
        submit_code_button.click()


    def error_handling(self):
        pass





if __name__ == '__main__':
    bot = FifaBot()
    bot.transfer.transfers()
    bot.transfer.search_transfer_market()
