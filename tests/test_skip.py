"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser
from selene.support.shared.jquery_style import s

size_windows = [(1980, 1080, "desktop"),
                (1600, 1200, "desktop"),
                (1280, 960, "desktop"),
                (428, 926, "mobile"),
                (372, 812, "mobile"),
                (414, 896, "mobile")]

#фикстура для разрещения экранов

@pytest.fixture(params=size_windows)
def size_windows_gadget(request):
    return request.param

#общий тест для мобилок и декстопа

def test_browser_size(size_windows_gadget):
    if size_windows_gadget[0] > 786:
        test_github_desktop(size_windows_gadget)
    if size_windows_gadget[0] < 786:
        test_github_mobile(size_windows_gadget)

# тест для декстопа

def test_github_desktop(size_windows_gadget):
    browser.open('')
    browser.driver.set_window_size(size_windows_gadget[0],
                                   size_windows_gadget[1])
    s('.HeaderMenu-link--sign-in').click()

# тест для мобилок

def test_github_mobile(size_windows_gadget):
    browser.open('')
    browser.driver.set_window_size(size_windows_gadget[0],
                                    size_windows_gadget[1])
    s('.flex-column [aria-label="Toggle navigation"]').click()
