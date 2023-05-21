"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser
from selene.support.shared.jquery_style import s

param_windows_desktop = [(1980, 1080),
                         (1600, 1200),
                         (1280, 960)]

param_windows_mobile = [(428, 926),
                        (372, 812),
                        (414, 896)]


@pytest.fixture(params=param_windows_desktop)
def param_windows_desktop(request):
    return request.param


def test_github_desktop(param_windows_desktop):
    browser.open('')
    browser.driver.set_window_size(param_windows_desktop[0], param_windows_desktop[1])
    s('.HeaderMenu-link--sign-in').click()


@pytest.fixture(params=param_windows_mobile)
def param_windows_mobile(request):
    return request.param


def test_github_mobile(param_windows_mobile):
    browser.open('')
    browser.driver.set_window_size(param_windows_mobile[0], param_windows_mobile[1])
    s('.flex-column [aria-label="Toggle navigation"]').click()
