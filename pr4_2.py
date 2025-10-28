n = 7

a = [[0 if j < n - 1 - i else n - (j - (n - 1 - i)) for j in range(n)] for i in range(n)]

for r in a:
    print(*r)