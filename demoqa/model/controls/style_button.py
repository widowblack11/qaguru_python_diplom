from selene import have


def border_color(color):
    return have.css_property('border-color', color)
