import pytest
from selene.support.shared.jquery_style import s
from selene import browser, have
from selene.support.shared import browser

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
@pytest.mark.parametrize("permision_w", [
    (1920, 1080),
    (1600, 900),
    (1600, 1024),
    (1280, 720),
])
def test_github_desktop(permision_w):
    browser.driver.set_window_size(permision_w[0], permision_w[1])
    browser.open('https://github.com/')
    s('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize("permision_m", [
    (428, 926),
    (372, 812),
    (414, 896),
    (414, 736)
])
def test_github_mobile(permision_m):
    browser.driver.set_window_size(permision_m[0],permision_m[1])
    browser.open('https://github.com/')
    s('.flex-column [aria-label="Toggle navigation"]').click()
