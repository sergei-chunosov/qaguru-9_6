import sys
from datetime import time


def check_time(current_time):
    if current_time >= time(hour=22) or current_time <= time(hour=6):
        is_dark_theme = True
        print('Dark theme is enable')
    else:
        is_dark_theme = False
        print('Dark theme is disable')
    return is_dark_theme


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    is_dark_theme = check_time(current_time)
    print(is_dark_theme)

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    is_dark_theme = None
    if dark_theme_enabled_by_user:
        is_dark_theme = dark_theme_enabled_by_user
    else:
        is_dark_theme = check_time(current_time)

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = None

    for i in users:
        if i['name'] == 'Olga':
            suitable_users = i

    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []

    for i, v in enumerate(users):
        if v['age'] < 20:
            suitable_users.append(users[i])

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def func_print():
    func_name = sys._getframe(1).f_code.co_name
    get_attr = sys._getframe(1).f_locals
    name = (' '.join(func_name.split('_'))).title()
    list = []
    for attr in get_attr.values():
        list.append(attr)
    attr = ', '.join(list)
    print(name, attr)
    return f'{name} [{attr}]'


def open_browser(browser_name):
    actual_result = func_print()
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = func_print()
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = func_print()
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"




# def time():
#     time = True
#     if time:
#         print(time)
#     else:
#         print(f'False: time')
#
# time()