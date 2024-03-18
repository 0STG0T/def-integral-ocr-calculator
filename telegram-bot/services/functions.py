from math import sqrt


def rectangle_method(f, left, right, n):
    """
    Вычисляет определенный интеграл функции f(x) на отрезке [a, b] методом прямоугольников.
    :param f: Функция, которую нужно интегрировать.
    :param left: Левая граница отрезка.
    :param right: Правая граница отрезка.
    :param n: Количество прямоугольников (шаг разбиения).
    :return: Приближенное значение интеграла.
    """
    h = (right - left) / n
    integral_sum = sum(f(left + i * h) for i in range(n))
    return h * integral_sum


def trapezoid_method(f, left, right, n):
    """
    Вычисляет определенный интеграл функции f(x) на отрезке [a, b] методом трапеций.
    :param f: Функция, которую нужно интегрировать.
    :param left: Левая граница отрезка.
    :param right: Правая граница отрезка.
    :param n: Количество трапеций (шаг разбиения).
    :return: Приближенное значение интеграла.
    """
    h = (right - left) / n
    integral_sum = sum((f(left + i * h) + f(left + (i + 1) * h)) for i in range(n))
    return h * integral_sum / 2


# Пример использования:


def simpson_method(f, left, right, n):
    """
    Вычисляет определенный интеграл функции f(x) на отрезке [a, b] методом Симпсона.
    :param f: Функция, которую нужно интегрировать.
    :param left: Левая граница отрезка.
    :param right: Правая граница отрезка.
    :param n: Количество интервалов (шаг разбиения, должно быть четным).
    :return: Приближенное значение интеграла.
    """
    h = (right - left) / n
    integral_sum = f(left) + f(right) + 4 * sum(f(left + i * h) for i in range(1, n, 2)) + 2 * sum(
        f(left + i * h) for i in range(2, n - 1, 2)
    )
    return h * integral_sum / 3


def my_function(x):
    return sqrt(5 * x + 9)


def test():
    left, right = 0, 2  # Границы отрезка
    n = 100  # Количество прямоугольников
    result = rectangle_method(my_function, left, right, n)
    print(f"Приближенное значение интеграла (rctg): {result}")

    result = trapezoid_method(my_function, left, right, n)
    print(f"Приближенное значение интеграла (trpz): {result}")

    result = simpson_method(my_function, left, right, n)
    print(f"Приближенное значение интеграла (smps): {result}")
