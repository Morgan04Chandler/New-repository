a = str(input("Enter the sentence: "))

count = 0
for i in a.split():
    if i.endswith("r"):
        count += 1

print("Number of words ending in r:", count)