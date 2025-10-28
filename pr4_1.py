while True:
    try:
        N = int(input("Enter the length of the array: "))
        if N > 0:
            break
        else:
            print("Array length must be greater than 0.")
    except ValueError:
        print("Please enter an integer.")

arr = []
for i in range(N):
    while True:
        try:
            num = float(input(f"Enter the element {i+1}: "))
            arr.append(num)
            break
        except ValueError:
            print("Please enter a real number.")

p = [x for x in arr if x > 0]

print("Positive elements in reversed order:")
p.sort (reverse = True)
print(p)