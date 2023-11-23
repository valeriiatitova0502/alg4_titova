n = int(input())
etazh = 0
kol_probel = 1
probel = ' '
zvezd = '*'
for j in range(1, n + 1):
    etazh += 1
    kol_probel = n - etazh
    probel = probel * kol_probel
    if j == n:
        print(zvezd)
    else:
        print(probel + zvezd)
    probel = ' '
    zvezd += '*' * 2