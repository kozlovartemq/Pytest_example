import unittest
import pytest
from fixtures import web_driver_init
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.mark.runthis
class TestSelenium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
                                            # func names must starts with 'test_'
    def test_SearchInYandex(self) -> None:  # -> means type annotation for the func (returns None), can be -> str
        """Поиск в Яндексе"""
        driver = self.driver
        driver.get("https://yandex.ru")
        search_field = driver.find_element(By.XPATH, "//input[@name='text']")
        search_field.send_keys('XPath for beginners')
        search_field.send_keys(Keys.ENTER)

        self.assertTrue("Результаты поиска" in driver.page_source)  # expectation

    def tearDown(self) -> None:
        self.driver.close()


