import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('driver')
class TestSearch():

  def test_valid_search(self, driver):
    driver.get("https://ecommerce-playground.lambdatest.io/")
    search_field = driver.find_element(By.NAME, "search")
    search_field.send_keys("iphone")
    submit_button = driver.find_element(By.XPATH, '//*[@id="search"]/div[2]/button')
    submit_button.click()

