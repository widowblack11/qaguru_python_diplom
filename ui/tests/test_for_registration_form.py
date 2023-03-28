from demoqa.model.pages import practice_form


def test_practice_form(setup_browser):
    practice_form.open_page_practice_form()

    # Заполнить регистрационную форму
    practice_form.data_fill(firstName='Оксана', lastName='Прокопенко',
                            userEmail='proyeillepebe-2165@yopmail.com', gender='Female', Number='1234567890',
                            file='resource/test_5.jpeg', year='1998', month='0', day='01',
                            Subjects='Arts', Hobbies='Sports', State='NCR', City='Noida', Address='Краснодарский край')

    # Отправить форму регистрации
    practice_form.send_form()

    # Проверить корректность данных в заполненной форме
    practice_form.check_get_form(firstName='Оксана', lastName='Прокопенко', userEmail='proyeillepebe-2165@yopmail.com', gender='Female',
                             Number='1234567890', file='test_5.jpeg',
                             date='01 January,1998', Subjects='Arts', Hobbies='Sports', State='NCR',
                             City='Noida', Address='Краснодарский край')

    # Закрыть форму
    practice_form.close_form()
