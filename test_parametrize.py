from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github(browser_set):  # Убираем параметризацию, используем фикстуру
    device = browser_set  # Получаем текущий параметр фикстуры

    browser.open("https://github.com")

    if device == "mobile":
        s(".Button-label").click()  # Открываем бургер-меню перед Sign in

    else:  # Desktop
        s(".HeaderMenu-link--sign-in").should(be.clickable).click()  # Кликаем сразу, без бургер-меню
