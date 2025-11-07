def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("Файл", file_name, "не вдалося відкрити.")
        return None
    else:
        print("Файл", file_name, "відкрито.")
        return file


file1_name = "TF7_1.txt"
file2_name = "TF7_2.txt"

file_1_w = Open(file1_name, "w")

if file_1_w is not None:
    file_1_w.write("Письменник записав у щоденнику свої враження про осіннє місто. "
                   "Маленьке кошеня сиділо на підвіконні й дивилося на дощ. "
                   "Ми бачили панну, що йшла алеєю до старого будинку.")
    print("Інформацію додано у TF7_1.txt.")
    file_1_w.close()
    print("Файл TF7_1.txt закрито.")

file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_2_r is not None and file_2_w is not None:
    text = file_2_r.read()
    words = [word.strip(".,!?;:") for word in text.split()]

    doubled_words = []
    for word in words:
        for i in range(len(word) - 1):
            if word[i].lower() == word[i + 1].lower():
                doubled_words.append(word)
                break

    if doubled_words:
        for w in doubled_words:
            file_2_w.write(w + "\n")
    else:
        file_2_w.write("Слів з подвоєними літерами не знайдено.")

    file_2_r.close()
    file_2_w.close()
    print("Файли закрито.")

print("\nВміст файлу TF7_2.txt:")
file_3_r = Open(file2_name, "r")

if file_3_r is not None:
    for line in file_3_r:
        print(line.strip())
    file_3_r.close()
    print("Файл TF7_2.txt закрито.")
