import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time

def setup_function():
    global driver
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get("https://stage.alnafi.com/auth/sign-in")
    driver.maximize_window()

    driver.implicitly_wait(5)
def teardown_function():
    driver.quit

def my_cred():
    return [
        ('engribadkhan96@gmail.com','Engr@1122'),
        ('ibadsahil654@gmail.com', 'affan1122')
    ]
@pytest.mark.parametrize("username,password",my_cred())
def test_login(username,password):
    print("My pytest login")
    driver.find_element(By.NAME,'email').send_keys(username)
    time.sleep(3)
    driver.find_element(By.NAME, 'password').send_keys(password)
    time.sleep(3)