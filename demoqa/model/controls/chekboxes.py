from selene import have


class Chekboxes:
    def __init__(self, browser):
        self.browser = browser

    def select_chekbox(self, selector, value):
        self.browser.all(selector).element_by(have.exact_text(value)).click()
