import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", params=[(1920, 1080)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()

@pytest.fixture(scope="function", params=[(420,820)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()

@pytest.fixture(scope="function", params=[(1920, 1080), (420,820)])
def browser_set(request):
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"

    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 900:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()

