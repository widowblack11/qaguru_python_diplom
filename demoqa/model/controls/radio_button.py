from selene.support.conditions import have
from selene.support.shared import browser


def select_radio(selector, value):
    browser.all(selector).element_by(have.value(value)).element('..').click()