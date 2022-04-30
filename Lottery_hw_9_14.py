from random import choice
"""9.14. Лотерея: создайте список или кортеж,
содержащий серию из 10 чисел и 5 букв.
Слу-чайным образом выберите 4 числа или буквы из списка.
Выведите сообщение о том, что билет,
содержащий эту комбинацию из четырех цифр или букв, является выигрышным.
"""
"""
9.15. Анализ лотереи: напишите цикл, который проверяет, насколько сложно
выиграть в смоделированной вами лотерее.
Создайте список или кортеж с именем my_ticket.
Напишите цикл, который продолжает генерировать комбинации до тех пор,
пока не выпадет выигрышная комбинация.
Выведите сообщение с информацией о том, сколько выполнений
цикла понадобилось для получения выигрышной комбинации.
"""


class Lottery:
    """Класс генерирующий лотерею."""
    def __init__(self, numbers):
        self.random_list = None
        self.win_ticket = None
        self.number = numbers  # Принимаем список с символами.

    def lottery(self):
        """Генерируем выигрышный билет."""
        self.win_ticket = []
        for _ in range(4):  # Костыль для генерации четырех случайных символов.
            random = choice(self.number)
            self.win_ticket.append(random)
        print(f"Этот билет победил: {self.win_ticket}")

    def len_chance(self):
        """Считаем количество итераций."""
        a = []  # Считаем количество итераций.
        while True:
            self.random_list = []
            for _ in range(4):  # Костыль для генерации №2.
                random = choice(self.number)
                self.random_list.append(random)
            a.append(self.random_list)
            if self.random_list == self.win_ticket:
                break

        print(f"Количество итераций: {len(a)}")


number = Lottery(numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                          'a', 'b', 'c', 'd', 'e'])
number.lottery()
number.len_chance()
