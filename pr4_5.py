def m(A, x):

    if x in A:
        A.remove(x)
    else:
        A.add(x)

    return A

A_input = input("Enter the elements of set A separated by a 'SPACE': ")
A = set(A_input.split())

while True: #перевіримо щоб х був наявний та лише один
    x = input("Enter 'x': ").strip()
    if len(x) == 0:
        print("'x' is empty. Please try again.")
    elif len(x) > 1:
        print("'x' must be single. Please try again.")
    else:
        break

B = m(A, x)

print("New set B: ", B)