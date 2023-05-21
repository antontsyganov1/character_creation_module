from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def Calculate_Square_Root(Number) -> float:
    """Вычисляет квадратный корень."""
    fff = sqrt(Number)
    return fff


def calc(your_number):
    """Проверка числа."""
    if your_number <= 0:
        return
    else:
        Calculate_Square_Root(your_number)
        print(f"Мы вычислили квадратный корень из введённого вами числа."
              f" Это будет: {fff}")


calc(25.5)
