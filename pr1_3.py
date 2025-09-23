N = int(input("Enter N: "))
while N <= 1 or N >= 9:
    N = int(input("Enter N between 1 and 9: "))
for i in range(N):
    for j in range(N, i, -1):
        print(j, end=" ")
    print(" ")
