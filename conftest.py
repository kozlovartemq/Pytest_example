import pytest

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

def pytest_runtest_setup(item):
    print("\nTestSetup")

def pytest_runtest_call(item):
    print("\nIn runtest_call")

def pytest_runtest_teardown(item, nextitem):
    print("\nIN runtest_teardown")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    print("IN HOOK BEFORE yield")
    outcome = yield
    rep = outcome.get_result()
    rep.when
    print("REP IS " + str(rep) + "\nrep.when IS " + str(rep.when))
