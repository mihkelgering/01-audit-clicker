from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def login(username, password, driver):
    wait = WebDriverWait(driver, 5)
    name = wait.until(EC.presence_of_element_located((By.ID, "email-field")))
    name.send_keys(username)

    pw = wait.until(EC.presence_of_element_located((By.ID, "password-field")))
    pw.send_keys(password)

    sign_in = wait.until(EC.presence_of_element_located(
        (By.ID, "authenticate-button")))

    sign_in.click()
