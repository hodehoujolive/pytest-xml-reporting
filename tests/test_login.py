import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('driver')
class TestLogin():

  def test_valid_credentials(self, driver):
    driver.get("https://ecommerce-playground.lambdatest.io/")
    account_button = driver.find_element(By.XPATH, '//*[@id="widget-navbar-217834"]/ul/li[6]/a/div/span')
    account_button.click()

    time.sleep(5)

    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("email@email.com")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("email")


    login_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/form/input[1]')
    login_button.click()


