def n(lst):

    s = sorted(lst) #сортуємо список за зростанням
    return s[:5] #беремо зріз перших 5 чисел

u = input("Enter list items separated by a 'SPACE': ")

lst = [float(x) for x in u.split()]

m = n(lst)

print("The first five minimum elements: ", m)