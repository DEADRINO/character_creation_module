from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    sqrt(number)
    return number


def calc(your_number: float) -> float:
    """Возвращает число, чтобы вычислить квадратный корень."""
    if your_number <= 0:
        return your_number
    num = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа.'
          'Это будет: ' + str(num))


calc(25.5)
