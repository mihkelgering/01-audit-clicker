
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login
from configValidation import is_config_valid
from audit import fill_audit
import json
import os
import time

# Loading the config.
with open("config.json") as f:
    config = json.load(f)

# Checking if the config is valid.
if not is_config_valid(config):
    print("Config is not valid")
    exit()

# Checking if the path exists.
if not os.path.exists(config["chromedriver_path"]):
    print("Path does not exist")
    exit()

# Starting the driver.
driver = webdriver.Chrome(config["chromedriver_path"])

# define a wait time
wait = WebDriverWait(driver, 10)

# Open the login page.
driver.get('https://01.kood.tech/')

# Login.
login(config["nickname"], config["pw"], driver)

# Open the audit page.
driver.get(config["audit_url"])

# Fill the audit.
fill_audit(config, driver, wait)

# Close the driver.
driver.quit()
