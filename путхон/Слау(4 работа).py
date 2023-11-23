import copy, numpy
import numpy as np

a = numpy.array([[3.78, 3.44, 3.02, 46.81],
                 [4.33, 3.88, 3.39, 53.43],
                 [4.76, 4.24, 3.72, 58.73]])
print(a)


def gaussFunc(a):
    eps = 1e-16

    c = numpy.array(a)
    a = numpy.array(a)

    len1 = len(a[:, 0])  # Определение количества строк в матрице
    len2 = len(a[0, :])  # Определение количества столбцов в матрице

    for g in range(len1):
        max = abs(a[g][g])  # Находим максимальный элемент в столбце g для выбора главного элемента
        my = g  # Индекс строки с максимальным элементом
        t1 = g
        while t1 < len1:
            if abs(a[t1][g]) > max:
                max = abs(a[t1][g])
                my = t1
            t1 += 1
        amain = float(a[g][g])  # Главный элемент
        z = g
        while z < len2:  # Нормализация строки
            a[g][z] = a[g][z] / amain
            z += 1
        j = g + 1

        while j < len1:  # Вычитание главной строки из нижележащих строк
            b = a[j][g]
            z = g
            while z < len2:
                a[j][z] = a[j][z] - a[g][z] * b
                z += 1
            j += 1
    a = backTrace(a, len1)  # Обратный ход метода Гаусса
    return a


class DetermExeption(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def backTrace(a, len1):  # Обратный ход
    a = numpy.array(a)
    i = len1 - 1
    while i > 0:
        j = i - 1
        while j >= 0:
            a[j][len1] = a[j][len1] - a[j][i] * a[i][len1]
            j -= 1
        i -= 1
    return a[:, len1]


def vectorN(c, a, len1):
    c = numpy.array(c)
    a = numpy.array(a)
    vectB = copy.deepcopy(c[:, len1])  # Копирование вектора свободных членов из матрицы c
    b = numpy.zeros((len1))  # Создание нулевого вектора b с размерностью len1
    i = 0

    while i < len1:
        j = 0
        while j < len1:
            b[i] += c[i][j] * a[j]  # Подсчет элементов вектора b
            j += 1
        i = i + 1

    c = copy.deepcopy(b)  # Копирование вектора b в c
    for i in range(len1):
        c[i] = abs(c[i] - vectB[i])  # Расчет разницы между элементами векторов c и vectB
    return c


b = gaussFunc(a)
print("Ответ:")
print(b)