import math
import numpy as np
#import solve
import matplotlib.pyplot as plt
import time

# массив для встроенного метода
a1 = []
# массив для алгоритма без округления
a2 = []
# массив для алгоритма с округлением до 3
a3 = []
# массив для алгоритма с округлением до 6
a4 = []

at1 = []
at2 = []
at3 = []
at4 = []

# размерность системы
size = range(3, 100)

# алгоритм без округления
def gauss(n):
    m = np.random.rand(n, n+1)
    t = time.time()
    for i in range(0, n):
        max_index = i
        for k in range(i + 1, n):
            if (math.fabs(m[k, i]) > math.fabs(m[max_index, i])):
                max_index = k
        for j in range(i, n + 1):
            z = m[i, j]
            m[i, j] = m[max_index, j]
            m[max_index, j] = z
        c = m[i, i]
        for j in range(i, n + 1):
            m[i, j] = (m[i, j]) / c
        for k in range(i + 1, n):
            b = m[k, i]
            for l in range(i, n + 1):
                m[k, l] = m[k, l] - b * m[i, l]
    x = np.zeros(n)
    x[n - 1] = m[n - 1, n] / m[n - 1, n - 1]
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = s + m[k, j] * x[j]
        x[k] = m[k, n] - s
        k = k - 1
    return x

# алгоритм с округлением
def gaussRounding(n, e):
    m = np.random.rand(n, n + 1)
    for i in range(0, n):
        max_index = i
        for k in range(i + 1, n):
            if (math.fabs(m[k, i]) > math.fabs(m[max_index, i])):
                max_index = k
        for j in range(i, n + 1):
            z = m[i, j]
            m[i, j] = m[max_index, j]
            m[max_index, j] = z
        c = m[i, i]
        for j in range(i, n + 1):
            m[i, j] = round(((m[i, j]) / c), e)
        for k in range(i + 1, n):
            b = m[k, i]
            for l in range(i, n + 1):
                m[k, l] = round((m[k, l] - b * m[i, l]), e)
    c = m[n - 1, n - 1]
    for j in range(n - 1, n):
        m[n - 1, j] = round((m[n - 1, j] / c), e)
    x = []
    for i in range(0, n):
        x.append(0)
    x[n - 1] = round((m[n - 1, n] / m[n - 1, n - 1]), e)
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = (s + m[k, j] * x[j])
        x[k] = round((m[k, n] - s), e)
        k = k - 1
    return x

# алгоритм без округления
def gaussNotGenerationMatrix(m, n):
    t = time.time()
    for i in range(0, n):
        max_index = i
        for k in range(i + 1, n):
            if (math.fabs(m[k, i]) > math.fabs(m[max_index, i])):
                max_index = k
        for j in range(i, n + 1):
            z = m[i, j]
            m[i, j] = m[max_index, j]
            m[max_index, j] = z
        c = m[i, i]
        for j in range(i, n + 1):
            m[i, j] = (m[i, j]) / c
        for k in range(i + 1, n):
            b = m[k, i]
            for l in range(i, n + 1):
                m[k, l] = m[k, l] - b * m[i, l]
    x = np.zeros(n)
    x[n - 1] = m[n - 1, n] / m[n - 1, n - 1]
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = s + m[k, j] * x[j]
        x[k] = m[k, n] - s
        k = k - 1
    return x

# алгоритм с округлением
def gaussNotGenerationMatrixRounding(m, n, e):
    for i in range(0, n):
        max_index = i
        for k in range(i + 1, n):
            if (math.fabs(m[k, i]) > math.fabs(m[max_index, i])):
                max_index = k
        for j in range(i, n + 1):
            z = m[i, j]
            m[i, j] = m[max_index, j]
            m[max_index, j] = z
        c = m[i, i]
        for j in range(i, n + 1):
            m[i, j] = round(((m[i, j]) / c), e)
        for k in range(i + 1, n):
            b = m[k, i]
            for l in range(i, n + 1):
                m[k, l] = round((m[k, l] - b * m[i, l]), e)
    c = m[n - 1, n - 1]
    for j in range(n - 1, n):
        m[n - 1, j] = round((m[n - 1, j] / c), e)
    x = []
    for i in range(0, n):
        x.append(0)
    x[n - 1] = round((m[n - 1, n] / m[n - 1, n - 1]), e)
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = (s + m[k, j] * x[j])
        x[k] = round((m[k, n] - s), e)
        k = k - 1
    return x

# создание рандомной матрицы для построения встроенного метода
def generationMatrix(n):
    matrix1 = np.random.rand(n, n)
    matrix2 = np.random.rand(n, 1)
    return [matrix1, matrix2]

# сравнение времени алгоритма с учетом формирования матриц
def chart1():
    for i in size:
        t1 = time.time()
        np.linalg.solve(generationMatrix(i)[0], generationMatrix(i)[1])
        a1.append(time.time() - t1)
        t1 = time.time()
        gauss(i)
        a2.append(time.time() - t1)
        t1 = time.time()
        gaussRounding(i, 3)
        a3.append(time.time() - t1)
        t1 = time.time()
        gaussRounding(i, 5)
        a4.append(time.time() - t1)
    fig, ax = plt.subplots()
    ax.set_title('Временные затраты с учётом формирования матриц')
    ax.set_xlabel('Размерность системы')
    ax.set_ylabel('Время, сек')
    plt.grid()
    plt.plot(size, a1, '-b')
    plt.plot(size, a3, '-g')
    plt.plot(size, a4, '-m')
    plt.legend(['Встроенный', 'Округление до 3', 'Округление до 5'])
    plt.show()

# сравнение времени алгоритма без учёта формирования матриц
def chart2():
    for i in size:
        m1 = np.random.rand(i, i)
        m2 = np.random.rand(i, 1)
        m3 = np.hstack((m1, m2))
        t1 = time.time()
        np.linalg.solve(m1, m2)
        at1.append(time.time() - t1)
        t1 = time.time()
        gaussNotGenerationMatrix(m3, i)
        at2.append(time.time() - t1)
        t1 = time.time()
        gaussNotGenerationMatrixRounding(m3, i, 3)
        at3.append(time.time() - t1)
        t1 = time.time()
        gaussNotGenerationMatrixRounding(m3, i, 6)
        at4.append(time.time() - t1)
    fig, ax = plt.subplots()
    ax.set_title('Временные затраты без учёта формирования матриц')
    ax.set_xlabel('Размерность системы')
    ax.set_ylabel('Время, сек')
    plt.grid()
    plt.plot(size, at1, '-b')
    plt.plot(size, at2, '-r')
    plt.legend(['Встроенный', 'Без округления'])
    plt.show()

chart1()
chart2()