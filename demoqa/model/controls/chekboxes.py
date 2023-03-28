from selene import have
from selene.support.shared import browser


def select_chekbox(selector, value):
    browser.all(selector).element_by(have.exact_text(value)).click()