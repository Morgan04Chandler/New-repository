from pr2_2_money import expression2

A = float(input("Enter monthly scholarship (A): "))
while True:
    B = float(input("Enter monthly living expenses: "))
    if B > A:
        break
    print("Expenses must be greater than the scholarship.")

needed_money = expression2(A, B)
print(f"The total amount to ask parents for: {needed_money:.2f} UAH")