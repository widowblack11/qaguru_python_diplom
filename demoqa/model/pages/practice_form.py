from datetime import datetime

from selene import be, have, Browser

from demoqa.model.controls.chekboxes import Chekboxes
from demoqa.model.controls.dropdown import Dropdown
from demoqa.model.controls.radio_button import RadioButton
from demoqa.model.controls.select_dates_on_the_calendar import SelectDate
from demoqa.utils import resource
from demoqa.utils.generatore_date import get_format_today


class FormPage:
    def __init__(self, browser):
        self.browser: Browser = browser
        self.gender_select = RadioButton(browser)
        self.select_checkbox = Chekboxes(browser)
        self.dropdown = Dropdown(browser)
        self.date_calendar = SelectDate(browser)

    def open_page_practice_form(self):
        self.browser.open('/automation-practice-form')

    @property
    def number_field(self):
        return self.browser.element('[id="userNumber"]')

# Заполнение формы регистрации
    def data_fill(self, firstName, lastName, userEmail, gender, Number,  file, year, month,
                  day, Subjects, Hobbies, State, City, Address):
        if firstName:
            self.browser.element('[id="firstName"]').should(be.blank).type(firstName)
        if lastName:
            self.browser.element('[id="lastName"]').should(be.blank).type(lastName)
        if userEmail:
            self.browser.element('[id="userEmail"]').should(be.blank).type(userEmail)

        self.gender_select.select_radio('[name=gender]', gender)
        self.number_field.should(be.blank).type(Number)
        if file:
            self.browser.element('#uploadPicture').set_value(resource.get_path(file))
        if year and month and day:
            self.date_calendar.select_dates_on_the_calendar('#dateOfBirthInput', year=year, month=month, day=day)
        if Subjects:
            self.browser.element('#subjectsInput').type(Subjects).press_enter()
        if Hobbies:
            self.select_checkbox.select_chekbox('.custom-checkbox', Hobbies)
        if State:
            self.dropdown.dropdown_react('3', State)
        if City:
            self.dropdown.dropdown_react('4', City)
        if Address:
            self.browser.element('#currentAddress').type(Address)

    # Отправка формы регистрации
    def send_form(self):
        self.browser.element('#submit').press_enter()

    def check_get_form(self, firstName, lastName, gender, Number, userEmail='',  file='', date='', Subjects='', Hobbies='', State='', City='', Address=''):
        self.browser.all('.table-responsive').all('tr').element(1).should(have.text(firstName))
        self.browser.all('.table-responsive').all('tr').element(1).should(have.text(lastName))
        self.browser.all('.table-responsive').all('tr').element(2).all('td').element(1).should(have.exact_text(userEmail))
        self. browser.all('.table-responsive').all('tr').element(3).all('td').element(1).should(have.exact_text(gender))
        self. browser.all('.table-responsive').all('tr').element(4).all('td').element(1).should(have.exact_text(Number))
        if not date:
            date = get_format_today()
        self.browser.all('.table-responsive').all('tr').element(5).all('td').element(1).should(have.exact_text(date))
        self.browser.all('.table-responsive').all('tr').element(6).all('td').element(1).should(have.exact_text(Subjects))
        self.browser.all('.table-responsive').all('tr').element(7).all('td').element(1).should(have.exact_text(Hobbies))
        location = ''
        if State or City:
            location = ' '.join([State, City])
        self.browser.all('.table-responsive').all('tr').element(10).all('td').element(1).should(have.exact_text(location))
        self.browser.all('.table-responsive').all('tr').element(8).all('td').element(1).should(have.exact_text(file))
        self.browser.all('.table-responsive').all('tr').element(9).all('td').element(1).should(have.exact_text(Address))

    def close_form(self):
        self.browser.element('#closeLargeModal').press_enter()








