import pytest
from selene.support.shared import browser
from selene import be, have


def test_search_for_the_expected_result(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_search_for_an_empty_result(open_browser):
    browser.element('[name="q"]').should(be.blank).type('ghjfdnhfgh').press_enter()
    browser.element('[id="topstuff"]').should(have.text('ничего не найдено.'))
