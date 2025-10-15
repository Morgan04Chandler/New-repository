import math

def expression1(alpha):
    cos_a = math.cos(alpha)
    z = cos_a ** 2 + cos_a ** 4
    return z

def expression2(scholarship, expenses):
    total_needed = 0
    expenses_current = expenses
    months = 10

    for i in range(months):
        total_needed += expenses_current - scholarship
        expenses_current *= 1.05 

    return total_needed

alpha = float(input("Enter alpha: "))
z_value = expression1(alpha)
print(f"z = {z_value:.4f}")

A = float(input("Enter monthly scholarship: "))
while True:
    B = float(input("Enter monthly living expenses: "))
    if B > A:
        break
    print("Expenses must be greater than the scholarship.")

needed_money = expression2(A, B)
print(f"The total amount to ask parents for: {needed_money:.2f} UAH")