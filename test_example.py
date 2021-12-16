import time

import pytest
from fixtures import web_driver_init
@pytest.mark.xfail
@pytest.mark.runthis
def test_onetest():
    print("test1 running...")
    fail = False
    assert fail, "Fail on purpose"

@pytest.mark.skip(reason="no needed for now")
@pytest.mark.runthis
def test_second(web_driver_init):
    print("test2 running...")
    driver = web_driver_init
    driver.get("https://google.com/")

@pytest.mark.parametrize("url", ["https://google.com/", "https://vk.com/", "https://yandex.ru/"])  # Создание тестовых наборов
def test_multiple_urls(web_driver_init, url):
    print("test3 running...")
    driver = web_driver_init
    driver.get(url)
    assert driver.current_url == url
