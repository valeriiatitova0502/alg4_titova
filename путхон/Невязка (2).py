import numpy as np
import math
import matplotlib.pyplot as plt

size = range(3, 100)

n1 = []
n2 = []
n3 = []
n4 = []

# метод гаусса
def gauss(n):
    A = np.random.uniform(0, 10, (n, n))
    b = np.random.uniform(0, 10, (n, 1))
    M = np.hstack((A, b))
    xx = np.linalg.solve(A, b)
    for i in range(0, n):
        m = i
        for k in range(i + 1, n):
            if (math.fabs(M[k, i]) > math.fabs(M[m, i])):
                m = k
        for j in range(i, n + 1):
            z = M[i, j]
            M[i, j] = M[m, j]
            M[m, j] = z
        c = M[i, i]
        for j in range(i, n + 1):
            M[i, j] = (M[i, j]) / c
        for k in range(i + 1, n):
            b = M[k, i]
            for l in range(i, n + 1):
                M[k, l] = M[k, l] - b * M[i, l]
    c = M[n - 1, n - 1]
    for j in range(n - 1, n):
        M[n - 1, j] = M[n - 1, j] / c
    x = np.zeros(n)
    x[n - 1] = M[n - 1, n] / M[n - 1, n - 1]
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = s + M[k, j] * x[j]
        x[k] = M[k, n] - s
        k = k - 1
    d1 = 0
    for i in range(0, n - 1):
        d1 = d1 + (xx[i] - x[i]) ** 2
    d = (1.0 / n) * math.sqrt(d1.item())
    n1.append(d)
    e1 = 6
    for i in range(0, n):
        m = i
        for k in range(i + 1, n):
            if (math.fabs(M[k, i]) > math.fabs(M[m, i])):
                m = k
        for j in range(i, n + 1):
            z = M[i, j]
            M[i, j] = M[m, j]
            M[m, j] = z
        c = M[i, i]
        for j in range(i, n + 1):
            M[i, j] = round(((M[i, j]) / c), e1)
        for k in range(i + 1, n):
            b = M[k, i]
            for l in range(i, n + 1):
                M[k, l] = round((M[k, l] - b * M[i, l]), e1)
    c = M[n - 1, n - 1]
    for j in range(n - 1, n):
        M[n - 1, j] = round((M[n - 1, j] / c), e1)
    x3 = np.zeros(n)
    x3[n - 1] = round((M[n - 1, n] / M[n - 1, n - 1]), e1)
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = (s + M[k, j] * x3[j])
        x3[k] = round((M[k, n] - s), e1)
        k = k - 1
    d31 = 0
    for i in range(0, n - 1):
        d31 = d31 + (xx[i].item() - x3[i]) ** 2
    d3 = (1.0 / n) * math.sqrt(d31)
    n2.append(d3)
    e = 3
    for i in range(0, n):
        m = i
        for k in range(i + 1, n):
            if (math.fabs(M[k, i]) > math.fabs(M[m, i])):
                m = k
        for j in range(i, n + 1):
            z = M[i, j]
            M[i, j] = M[m, j]
            M[m, j] = z
        c = M[i, i]
        for j in range(i, n + 1):
            M[i, j] = round(((M[i, j]) / c), e)
        for k in range(i + 1, n):
            b = M[k, i]
            for l in range(i, n + 1):
                M[k, l] = round((M[k, l] - b * M[i, l]), e)
    c = M[n - 1, n - 1]
    for j in range(n - 1, n):
        M[n - 1, j] = round((M[n - 1, j] / c), e)
    x2 = np.zeros(n)
    x2 = np.zeros(n)
    x2[n - 1] = round(M[n - 1, n] / M[n - 1, n - 1], e)
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = (s + M[k, j] * x2[j])
        x2[k] = round((M[k, n] - s), e)
        k = k - 1
    d21 = 0
    for i in range(0, n - 1):
        d21 = d21 + (xx[i].item() - x2[i]) ** 2
    d2 = (1.0 / n) * math.sqrt(d21)
    n3.append(d2)

# точка невязки
def dot():
    A = np.array([[3.78, 3.44, 3.02],
                  [4.33, 3.88, 3.39],
                  [4.76, 4.24, 3.72]])

    B = np.array([[46.81], [53.43], [58.73]])
    dot_x = 3
    dot_y = 0.000197642353752
    return dot_x, dot_y

# точка невязки 6x6
def dot2():
    dot2_x = 5
    dot2_y = 0.000004661414006
    return dot2_x, dot2_y

# вывод графика
def chart():
    for i in size:
        gauss(i)
        A = np.random.uniform(0, 10, (5, 5))
        b = np.random.uniform(0, 10, (5, 1))
        x_exact = np.linalg.solve(A, b)
        x_builtin = np.linalg.solve(A, b)
        residual = np.mean(np.abs(x_exact - x_builtin))
        n4.append(residual)
    x, y = dot()
    x2, y2 = dot2()
    fig, ax = plt.subplots()
    plt.plot(size, n1, 'r-', label='без округления')
    plt.plot(size, n3, linestyle='-', color='lime', label='округление до 3')
    plt.plot(size, n2, 'b-', label='округление до 5')
    plt.plot(size, n4, '*g', label='невязка 3x3')
    plt.plot(x, y, '*g', label='невязка 3x3')
    plt.plot(x2, y2, '*b', label='невязка 5x5')
    ax.set_xlabel('Размер')
    ax.set_ylabel('Невязка')
    ax.set_title('График невязки')
    ax.legend(bbox_to_anchor=(0.5, -0.2), loc='upper center')
    plt.legend(['без округления', 'округление до 3', 'округление до 5', 'невязка 3x3', 'невязка 5x5'])
    plt.yscale('log')
    plt.grid()
    plt.show()

chart()