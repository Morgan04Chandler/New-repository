a = int(input ("Enter a: "))
while (a <= 0):
    a = int(input ("Enter a greater than zero: "))
b = int(input ("Enter b: "))
while (b <= 0):
    b = int(input ("Enter b greater than zero: "))
if a < b:
    r = a / b + 1
elif a == b:
    r = -1
else:
    r = (a * b - 5) / a
print("Result: " , r)

