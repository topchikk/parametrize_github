import pytest
from selene import browser, by


def test_desktop(browser_set):
    if browser_set == "mobile":
        pytest.skip("Мобильное разрешение")
    browser.open("https://github.com")
    browser.element(by.text("Sign up")).click()

def test_mobile(browser_set):
    if browser_set == "desktop":
        pytest.skip("Десктопное разрешение")
    browser.open("http://github.com")
    browser.element("[class='Button-content']").click()
    browser.element(by.text("Sign up")).click()