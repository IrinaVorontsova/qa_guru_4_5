from datetime import time
import pytest

def test_dark_theme():
    """
    Протестируйте правильность переключения темной темы на сайте
    """
    current_time = time(hour=23)
    if time(hour=6) <= current_time or current_time >= time(hour=22):
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True

    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    current_time = time(hour=16)
    dark_theme_enabled = True

    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную
    if time(hour=6) <= current_time or current_time >= time(hour=22) or dark_theme_enabled:
        is_dark_theme = True
    else:
        is_dark_theme = False

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

    suiable_user = [user for user in users if user['name'] == 'Olga']
    suiable_user = suiable_user[0]

    assert suiable_user == {"name": "Olga", "age": 45}
    # TODO найдите всех пользователей младше 20 лет

    suiable_users = [user for user in users if user['age'] < 20]

    assert suiable_users == [
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

def change_function_name(function, **kwargs):
    return f'''{function.__name__.replace('_', ' ').title()} {str(list(kwargs.values())).replace("'", "")}'''

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def open_browser(browser_name):
    actual_result = change_function_name(open_browser, browser_name=browser_name)
    assert actual_result == "Open Browser [Chrome]"

def go_to_companyname_homepage(page_url):
    actual_result = change_function_name(go_to_companyname_homepage, page_url=page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = change_function_name(find_registration_button_on_login_page, page_url=page_url, button_text=button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
