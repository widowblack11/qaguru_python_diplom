import allure
from allure_commons.types import Severity

from demoqa.data.constant import RED_COLOR
from demoqa.model.controls.style_button import border_color
from demoqa.model.pages.practice_form import FormPage


@allure.title('Успешная регистрация по всеми полями')
@allure.tag('web')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Регистрация')
@allure.story('DemoQA')
def test_successful_registration_with_all_fields(setup_browser):
    form_page = FormPage(setup_browser)
    with allure.step('Открыть страницу регистрации'):
        form_page.open_page_practice_form()

    with allure.step('Заполнить все поля'):
        form_page.data_fill(firstName='Оксана', lastName='Прокопенко',
                            userEmail='proyeillepebe-2165@yopmail.com', gender='Female', Number='1234567890',
                            file='resource/test_5.jpeg', year='1998', month='0', day='01',
                            Subjects='Arts', Hobbies='Sports', State='NCR', City='Noida', Address='Краснодарский край')

    with allure.step('Отправить форму'):
        form_page.send_form()

    with allure.step('Проверить, что в полученной форме все поля соответствует ранее заполненной информации'):
        form_page.check_get_form(firstName='Оксана', lastName='Прокопенко', userEmail='proyeillepebe-2165@yopmail.com', gender='Female',
                                 Number='1234567890', file='test_5.jpeg',
                                 date='01 January,1998', Subjects='Arts', Hobbies='Sports', State='NCR',
                                 City='Noida', Address='Краснодарский край')

    with allure.step('Закрыть форму'):
        form_page.close_form()


@allure.title('Регистрация только с обязательными полями')
@allure.tag('web')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Регистрация')
@allure.story('DemoQA')
def test_registration_only_with_required_fields(setup_browser):
    form_page = FormPage(setup_browser)
    with allure.step('Открыть страницу регистрации'):
        form_page.open_page_practice_form()

    with allure.step('Заполнить форму регистрации только обязательными полями'):
        form_page.data_fill(firstName='Иван', lastName='Иванов',
                            userEmail=None, gender='Female', Number='1234567890',
                            file=None, year=None, month=None, day=None,
                            Subjects=None, Hobbies=None, State=None, City=None, Address=None)

    with allure.step('Отправить форму'):
        form_page.send_form()

    with allure.step('Проверить, что в полученной форме все поля соответствует ранее заполненной информации, '
                     'а не заполненные поля пустые'):
        form_page.check_get_form(firstName='Иван', lastName='Иванов', gender='Female', Number='1234567890')

    with allure.step('Закрыть форму'):
        form_page.close_form()


@allure.title('Регистрация с телефоном невалидного формата')
@allure.tag('web')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Регистрация')
@allure.story('DemoQA')
def test_registration_with_invalid_phone_number(setup_browser):
    form_page = FormPage(setup_browser)
    with allure.step('Открыть страницу регистрации'):
        form_page.open_page_practice_form()

    with allure.step('Заполнить поле форму регистрации номер телефона невалидного формата'):
        form_page.data_fill(firstName=None, lastName=None,
                            userEmail=None, gender='Female', Number='123456789',
                            file=None, year=None, month=None, day=None,
                            Subjects=None, Hobbies=None, State=None, City=None, Address=None)

    with allure.step('Отправить форму'):
        form_page.send_form()
    with allure.step('Проверить,что рамка поля ввода номера телефона окрашена в цвет согласно макету'):
        form_page.number_field.should(border_color(RED_COLOR))




