class Dropdown:
    def __init__(self, browser):
        self.browser = browser

    def dropdown_react(self, id_option, text):
     self.browser.element(f'#react-select-{id_option}-input').type(text).press_enter()