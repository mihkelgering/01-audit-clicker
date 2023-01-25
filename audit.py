from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_audit(config, driver, wait):
    # Wait for the code input to appear.
    code_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@type='text']")))
    
    # Send the code.
    code_input.send_keys(config["audit_code"])
    
    # Wait for the radio buttons to appear.
    radio_buttons = WebDriverWait(driver, timeout=3).until(lambda d:
                                                           d.find_elements(By.XPATH, "//input[contains(@id, '-yes')]"))
    
    # Click the radio buttons.
    for button in radio_buttons:
        button.click()
        print("Clicked button")
    
    # Wait for the submit button to appear.
    submit_button = WebDriverWait(driver, timeout=10).until(
        lambda d: d.find_element(By.ID, "submit-btn"))

    # Click the submit button.
    submit_button.click()
    