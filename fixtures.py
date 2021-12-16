import pytest
from selenium import webdriver

"""
Порядок выполнения кода при использовании hook'ов и fixture одновременно:
1. pytest_runtest_setup(item) 
TestSetup
2. fixture до yield
Fixture before yield
PASSED                                      [100%]
3. pytest_runtest_call(item)
Inside the test call, start
4. тело теста
test2 running...
5. pytest_runtest_teardown(item, nextitem)
After test completed
6. fixture после yield
Fixture after yield

"""

@pytest.fixture()
def web_driver_init(request):
    """Init before a test"""
    print("\nFixture before yield")
    browser_name = request.config.option.browser_name
    if browser_name == "chrome":
        driver = webdriver.Chrome('./chromedriver.exe')
    elif browser_name == "firefox":
        # driver = webdriver.Firefox('./gekodriver.exe')
        raise ValueError("I dont have firefoxx browser yet")
    yield driver

    """Actions after a test"""
    print("\nFixture after yield")
    driver.close()
