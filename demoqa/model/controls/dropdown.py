from selene.support.shared import browser


def dropdown_react(id_option, text):
    browser.element(f'#react-select-{id_option}-input').type(text).press_enter()