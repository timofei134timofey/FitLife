"""Спринт 1"""


def check_age(qwery):
    """Вводим возраст"""
    try:
        user_age = int(input(qwery))
        assert user_age > 0, 'Возраст должен быть больше нуля'
    except ValueError:
        print('Ошибка: Введите число')
    except AssertionError as error:
        print('Ошибка:', error)
    else:
        return user_age


def check_weight(qwery):
    """Вводим вес"""
    try:
        user_weight = float(input(qwery))
        assert user_weight > 0, 'Вес должен быть больше нуля'
    except ValueError:
        print('Ошибка: Введите число')
    except AssertionError as error:
        print('Ошибка:', error)
    else:
        return user_weight


def check_height(qwery, typs):
    """Вводим рост"""
    try:
        user_height = typs(input(qwery))
        assert user_height > 0, 'Вес должен быть больше нуля'
    except ValueError:
        print('Ошибка: Введите число')
    except AssertionError as error:
        print('Ошибка:', error)
    else:
        return user_height


def calculation(user_weight, user_height):
    """Расчитываем остальное"""
    ML_IN_L = 1000
    ML_ON_KG = 30
    bmi: float = user_weight / (user_height ** 2)  # расчет индекса массы
    water_ml = user_weight * ML_ON_KG / ML_IN_L  # расчет нормы воды
    return bmi, water_ml


def show_message(user_name, user_age, user_weight, user_height):
    """Выводим сообщение"""
    bmi, water_ml = calculation(user_weight, user_height)
    # print(user_name, user_age, user_weight, user_height)
    print(f'''Отчет для пользователя: {user_name} ({user_age} г.)
Твой Индекс Массы Тела: {bmi:.1f}
Рекомендуемая норма воды: {water_ml} л. в день

Расчет окончен. Будьте здоровы!''')


def main():
    """Главная"""
    user_name: str = input('Как Вас зовут? ')  # Вводим имя
    user_age = check_age('Сколько Вам лет? ')
    user_weight: float = check_weight('Введите Ваш вес в кг ')
    user_height: float = check_height('Введите Ваш рост вес в метрах ', float)
    if user_name and user_age and user_weight and user_height:
        show_message(user_name, user_age, user_weight, user_height)


if __name__ == '__main__':
    main()
