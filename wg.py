import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def test_test2():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

        # Initialize WebDriver with options
        driver = webdriver.Chrome(options=chrome_options)
        command = "aws secretsmanager get-secret-value --secret-id securelinesecret --region us-east-1 --query SecretString --output text | awk -F'\"' '{pri>
        webgoatuser = os.popen(command).read().strip()
        command1 = "aws secretsmanager get-secret-value --secret-id securelinesecret --region us-east-1 --query SecretString --output text | awk -F'\"' '{pr>
        webgoatpassword = os.popen(command1).read().strip()
        print(webgoatuser)
        print(webgoatpassword)
#        driver = webdriver.Chrome()
        driver.get("http://sakharkar.in:30002/WebGoat/login")
        driver.set_window_size(1552, 832)
        driver.find_element(By.LINK_TEXT, "or register yourself as a new user").click()
        driver.find_element(By.ID, "username").send_keys(webgoatuser)
        driver.find_element(By.ID, "password").send_keys(webgoatpassword)
        driver.find_element(By.ID, "matchingPassword").click()
        driver.find_element(By.ID, "matchingPassword").send_keys(webgoatpassword)
        driver.find_element(By.NAME, "agree").click()
        driver.find_element(By.CSS_SELECTOR, ".btn").click()
        driver.close()
    except Exception as e:
        print("Something went wrong Error : " + str(e))


test_test2()
