"""Спринт 1"""


ML_IN_L = 1000
ML_ON_KG = 30


def check_age(qwery):
    """Вводим возраст"""
    while True:
        try:
            user_age = int(input(qwery))
        except ValueError:
            print('Ошибка: Введите число')
            continue
        if user_age <= 0:
            print('Возраст должен быть больше нуля')
            continue
        return user_age


def check_weight(qwery):
    """Вводим вес"""
    while True:
        try:
            user_weight = float(input(qwery))
        except ValueError:
            print('Ошибка: Введите число')
            continue
        if user_weight <= 0:
            print('Вес должен быть больше нуля')
            continue
        return user_weight


def check_height(qwery, typs):
    """Вводим рост"""
    while True:
        try:
            user_height = typs(input(qwery))
        except ValueError:
            print('Ошибка: Введите число')
            continue
        if user_height <= 0:
            print('Рост должен быть больше нуля')
            continue
        return user_height


def calculation(user_weight, user_height):
    """Расчитываем остальное"""
    bmi: float = user_weight / (user_height ** 2)  # расчет индекса массы
    water_ml = user_weight * ML_ON_KG / ML_IN_L  # расчет нормы воды
    return bmi, water_ml


def show_message(user_name, user_age, user_weight, user_height):
    """Выводим сообщение"""
    bmi, water_ml = calculation(user_weight, user_height)
    print(f"""Отчет для пользователя: {user_name} ({user_age} г.)
Твой Индекс Массы Тела: {bmi:.1f}
Рекомендуемая норма воды: {water_ml} л. в день

Расчет окончен. Будьте здоровы!""")


def main():
    """Главная"""
    user_name: str = input('Как Вас зовут? ')  # Вводим имя
    user_age = check_age('Сколько Вам лет? ')
    user_weight: float = check_weight('Введите вес в кг ')
    user_height: float = check_height(
        'Введите рост в метрах, используя точку: 1.75 ', float
    )
    show_message(user_name, user_age, user_weight, user_height)


if __name__ == '__main__':
    main()
