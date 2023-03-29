from selene.support.conditions import have


class RadioButton:
    def __init__(self, browser):
        self.browser = browser

    def select_radio(self, selector, value):
     self.browser.all(selector).element_by(have.value(value)).element('..').click()
