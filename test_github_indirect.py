import pytest
from selene import browser, by


@pytest.mark.parametrize("desktop_browser", [(1280, 720)], indirect=True)
def test_desktop_indirect(desktop_browser):
    browser.open("https://github.com/")
    browser.element(by.text("Sign up")).click()


@pytest.mark.parametrize("mobile_browser", [(800, 400)], indirect=True)
def test_mobile_indirect(mobile_browser):
    browser.open("https://github.com/")
    browser.element("[class='Button-content']").click()
    browser.element(by.text("Sign up")).click()
