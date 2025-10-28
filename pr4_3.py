def remove(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

user_input = input("Enter list elements separated by a 'SPACE': ")
lst = user_input.split()

removed = remove(lst)

print("List without repetitions:", removed)