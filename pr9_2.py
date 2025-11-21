import json
import os

FILE = "students.json"
RESULT_FILE = "birthday_result.json"

initial_students = [
    {"Surname": "Щербань", "Name": "Дарія", "Patronymic": "Миколаївна",
     "Birth": {"year": 2006, "month": 3, "day": 30}, "Sex": "F"},

    {"Surname": "Бачиш", "Name": "Павло", "Patronymic": "Геннадійович",
     "Birth": {"year": 2007, "month": 10, "day": 21}, "Sex": "M"},

    {"Surname": "Козинець", "Name": "Володимир", "Patronymic": "Андрійович",
     "Birth": {"year": 2007, "month": 6, "day": 10}, "Sex": "M"},

    {"Surname": "Гиренко", "Name": "Ілля", "Patronymic": "Романович",
     "Birth": {"year": 2006, "month": 11, "day": 2}, "Sex": "M"},

    {"Surname": "Сагайдак", "Name": "Богдан", "Patronymic": "Андрійович",
     "Birth": {"year": 2007, "month": 9, "day": 13}, "Sex": "M"},

    {"Surname": "Мартиненко", "Name": "Олександр", "Patronymic": "Володимирович",
     "Birth": {"year": 2006, "month": 5, "day": 24}, "Sex": "M"},

    {"Surname": "Репін", "Name": "Данііл", "Patronymic": "Вікторович",
     "Birth": {"year": 2006, "month": 7, "day": 25}, "Sex": "M"},

    {"Surname": "Голишев", "Name": "Артем", "Patronymic": "Антонович",
     "Birth": {"year": 2007, "month": 6, "day": 30}, "Sex": "M"},

    {"Surname": "Шкурат", "Name": "Дар'я", "Patronymic": "Андріївна",
     "Birth": {"year": 2007, "month": 11, "day": 2}, "Sex": "F"},

    {"Surname": "Біла", "Name": "Єлизавета", "Patronymic": "Сергіївна",
     "Birth": {"year": 2007, "month": 6, "day": 11}, "Sex": "F"}
]

if not os.path.exists(FILE):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(initial_students, f, ensure_ascii=False, indent=4)

def load_data():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def list():
    data = load_data()
    print("\nВміст файлу students.json")
    for s in data:
        print(s)
    print()

def add():
    data = load_data()
    print("\nВведіть дані нового учня:")
    surname = input("Прізвище: ")
    name = input("Ім'я: ")
    patronymic = input("По батькові: ")
    year = int(input("Рік народження: "))
    month = int(input("Місяць народження (1–12): "))
    day = int(input("День народження: "))
    sex = input("Стать (M/F): ")

    data.append({
        "Surname": surname,
        "Name": name,
        "Patronymic": patronymic,
        "Birth": {"year": year, "month": month, "day": day},
        "Sex": sex
    })

    save_data(data)
    print("Учня успішно додано.\n")

def delete():
    data = load_data()

    print("\nВведіть ПІБ учня, якого хочете видалити:")
    surname = input("Прізвище: ").strip()
    name = input("Ім'я: ").strip()
    patronymic = input("По батькові: ").strip()

    new_data = [
        s for s in data
        if not (
            s["Surname"].lower() == surname.lower() and
            s["Name"].lower() == name.lower() and
            s["Patronymic"].lower() == patronymic.lower()
        )
    ]

    if len(new_data) == len(data):
        print("Учня з таким ПІБ не знайдено.\n")
    else:
        save_data(new_data)
        print("Учня успішно видалено.\n")

def search():
    data = load_data()
    print("\nПоля для пошуку: Surname, Name, Sex")
    field = input("Оберіть поле пошуку: ")
    value = input("Введіть значення: ")

    result = [s for s in data if str(s.get(field, "")).lower() == value.lower()]

    if result:
        print("\nЗнайдені учні:")
        for r in result:
            print(r)
    else:
        print("Немає збігів.")
    print()

def birthday():
    data = load_data()
    month = int(input("Введіть номер місяця: "))

    result = [
        {"Surname": s["Surname"], "Name": s["Name"]}
        for s in data if s["Birth"]["month"] == month
    ]

    with open(RESULT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    if result:
        print("\nУчні з днем народження у цьому місяці:")
        for r in result:
            print(f"{r['Name']} {r['Surname']}")
    else:
        print("У цьому місяці ні в кого з учнів немає днів народження.")
    print()

while True:
    print("МЕНЮ")
    print("1. Вивести повний список учнів")
    print("2. Додати нового учня")
    print("3. Видалити учня")
    print("4. Пошук учня")
    print("5. Знайти учнів, які народилися у вказаному місяці")
    print("0. Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        list()
    elif choice == "2":
        add()
    elif choice == "3":
        delete()
    elif choice == "4":
        search()
    elif choice == "5":
        birthday()
    elif choice == "0":
        print("Вихід.")
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.\n")