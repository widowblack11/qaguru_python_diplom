from selene import be, have
from selene.support.shared import browser

from demoqa.model.controls.chekboxes import select_chekbox
from demoqa.model.controls.select_dates_on_the_calendar import select_dates_on_the_calendar
from demoqa.model.controls.dropdown import dropdown_react
from demoqa.model.controls.radio_button import select_radio


# Открытие формы регистрации
from demoqa.utils.resource import path_file


def open_page_practice_form():
    browser.open('/automation-practice-form')


# Заполнение формы регистрации
def data_fill(firstName, lastName, userEmail, gender, Number,  file, year, month,
              day, Subjects, Hobbies, State, City, Address ):
    browser.element('[id="firstName"]').should(be.blank).type(firstName)
    browser.element('[id="lastName"]').should(be.blank).type(lastName)
    browser.element('[id="userEmail"]').should(be.blank).type(userEmail)

    select_radio('[name=gender]', gender)
    browser.element('[id="userNumber"]').should(be.blank).type(Number)

    browser.element('#uploadPicture').set_value(path_file(file))

    select_dates_on_the_calendar('#dateOfBirthInput', year=year, month=month, day=day)

    browser.element('#subjectsInput').type(Subjects).press_enter()

    select_chekbox('.custom-checkbox', Hobbies)

    dropdown_react('3', State)
    dropdown_react('4', City)
    browser.element('#currentAddress').type(Address)


# Отправка формы регистрации
def send_form():
    browser.element('#submit').press_enter()


def check_get_form(userEmail, gender, Number,  file, date, Subjects, Hobbies, Address):
    browser.all('.table-responsive').all('tr').element(2).should(have.text(userEmail))
    browser.all('.table-responsive').all('tr').element(3).should(have.text(gender))
    browser.all('.table-responsive').all('tr').element(4).should(have.text(Number))
    browser.all('.table-responsive').all('tr').element(5).should(have.text(date))
    browser.all('.table-responsive').all('tr').element(6).should(have.text(Subjects))
    browser.all('.table-responsive').all('tr').element(7).should(have.text(Hobbies))
    browser.all('.table-responsive').all('tr').element(8).should(have.text(file))
    browser.all('.table-responsive').all('tr').element(9).should(have.text(Address))


def close_form():
    browser.element('#closeLargeModal').press_enter()




