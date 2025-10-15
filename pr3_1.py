while True:
    a = str(input("Enter word: "))

    if len(a) >= 5:
        last_5 = a[-5:]
        print("Last 5 characters:", last_5)
        break
    else:
        print("The word is too short to get the last 5 characters.")