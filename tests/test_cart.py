import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('driver')
class TestCart():

  def test_view_cart(self, driver):
    driver.get("https://ecommerce-playground.lambdatest.io/")
    cart_button = driver.find_element(By.XPATH, '//*[@id="entry_217825"]/a/div[1]')
    cart_button.click()

  def test_add_to_cart(self, driver):
    driver.get("https://ecommerce-playground.lambdatest.io/")
    product = driver.find_element(By.XPATH, 'INVALID XPATH')
    product.click()

    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="entry_216842"]/button')
    time.sleep(5)


