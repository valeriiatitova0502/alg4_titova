import time
import numpy as np
import math
from scipy.linalg import solve
import matplotlib.pyplot as plt

razm = range(100,120) #задается диапазон размерности матрицы

V = [] # это массивы, куда будут приходить значения вычисления времени,
V2 = [] # за какое будет считаться каждая матрица 
V3 = []# (размерности 100, 101, 102...130)


def M_Gauss(n):
    A = np.random.uniform(0, 10, (n, n)) 
    b = np.random.uniform(0, 10, (n, 1))
    M = np.hstack((A,b))
    
    #тут вычисляется значение матрицы встроенным методом
    d = time.time()
    solve(A, b) #встроенный метод
    D = time.time()-d # здесь получается ответ вычисления времени D
    V.append(D) #сюда приходят значения времени D
    
    #вычисление значения матрицы методом гаусса БЕЗ округления
    t = time.time()
    for i in range (0, n):
       m = i
       for k in range (i + 1, n):
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
    x = []
    for i in range(0, n):
        x.append(0)
    x[n - 1] = M[n - 1, n] / M[n - 1, n - 1]
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = s + M[k,j] * x[j]
        x[k] = M[k, n] - s 
        k = k - 1
    T=time.time()-t #получается значение времени T
    V2.append(T) #складываются T
    
    #вычисляется значение матрицы методом гаусса С ОКРУГЛЕНИЕМ до 3 (e) цифр после запятой
    e = 3 
    p = time.time()
    for i in range (0, n):
       m = i
       for k in range (i + 1, n):
           if (math.fabs(M[k, i]) > math.fabs(M[m, i])):
               m = k
       for j in range(i, n + 1):
           z = M[i, j]
           M[i, j] = M[m, j]
           M[m, j] = z
       c = M[i, i]
       for j in range(i, n + 1):
           M[i, j] = round(((M[i, j]) / c),e)
       for k in range(i + 1, n):
           b = M[k, i]
           for l in range(i, n + 1):
               M[k, l] = round((M[k, l] - b * M[i, l]),e)    
    c = M[n - 1, n - 1]
    for j in range(n - 1, n):
        M[n - 1, j] = round((M[n - 1, j] / c),e)
    x = []
    for i in range(0, n):
        x.append(0)
    x[n - 1] = round((M[n - 1, n] / M[n - 1, n - 1]),e)
    k = n - 2
    while k >= 0:
        s = 0
        for j in range(k + 1, n):
            s = (s + M[k,j] * x[j])
        x[k] = round((M[k, n] - s),e)
        k = k - 1
    P = time.time()-p
    V3.append(P) 
    
#тут высчитываются все матрицы размерности от 100 до 130 (прогоняется через razm)
for n in razm:
    t = time.time() 
    d = time.time()
    p = time.time()
    M_Gauss(n)
    

# отображение результатов
fig, ax = plt.subplots()
ax.set_xlabel('размерность')
ax.set_ylabel('временные затраты')

plt.plot(razm, V,'r-', label ='Встроенный метод')
plt.plot(razm, V2,'b-', label ='Алгоритм')
plt.plot(razm, V3,'g-', label ='Алг. с округлением')
ax.legend()
plt.grid()
plt.show()