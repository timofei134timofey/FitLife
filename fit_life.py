ML_IN_L = 1000
ML_ON_KG = 30


user_name: str = input('Как Вас зовут? ')  # Вводим именя
user_age: int = int(input('Сколько Вам лет? '))  # Вводим возраст
user_weight: float = float(input('Введите Ваш вес в кг '))  # Вводим вес
user_height: float = float(input('Введите Ваш рост в метрах '))  # Вводим рост

bmi: float = user_weight / (user_height ** 2)  # расчет индекса массы
water_ml = user_weight * ML_ON_KG / ML_IN_L  # расчет нормы воды

print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi:.1f}')
print(f'Рекомендуемая норма воды: {water_ml} л. в день')
print("Расчет окончен. Будьте здоровы!")
