from selene import browser, by


def test_desktop(desktop_browser):
    browser.open("http://github.com")
    browser.element(by.text("Sign up")).click()


def test_mobile(mobile_browser):
    browser.open("http://github.com")
    browser.element("[class='Button-content']").click()
    browser.element(by.text("Sign up")).click()