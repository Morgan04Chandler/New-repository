from datetime import date

def list(students):
    if not students:
        print("Словник порожній.")
    else:
        print("\nСписок учнів у класі:")
        for key, value in students.items():
            print(f"{key}: {value}")
    print()

def add(students):
    try:
        last_name = input("Введіть прізвище учня: ").strip()
        first_name = input("Введіть ім'я учня: ").strip()
        patronymic = input("Введіть по батькові учня: ").strip()
        key = f"{last_name} {first_name} {patronymic}"

        if key in students:
            print("Запис не додано, тому що учень з таким ПІБ вже існує.\n")
            return

        year = int(input("Рік народження учня: "))
        month = int(input("Місяць народження учня: "))
        day = int(input("День народження учня: "))

        students[f"{last_name} {first_name} {patronymic}"] = (year, month, day)
        print("Учня успішно додано!\n")
    except ValueError:
        print("Неправильний формат дати.\n")

def delete(students):
    key = input("Введіть ПІБ учня для видалення: ").strip()
    try:
        del students[key]
        print("Запис учня видалено.\n")
    except KeyError:
        print("Учня з таким ПІБ не знайдено.\n")

def sort(students):
    if not students:
        print("Словник порожній.\n")
        return

    print("\nСписок учнів за алфавітом:")
    for key in sorted(students.keys()):
        print(f"{key}: {students[key]}")
    print()

def birthday(students):
    today = date.today()
    found = False

    print(f"\nСьогодні: {today.day}.{today.month}.{today.year}")
    print("Учні, у яких сьогодні день народження:")

    for key, (year, month, day) in students.items():
        if day == today.day and month == today.month:
            found = True
            name_parts = key.split()
            print(f"- {name_parts[1]} {name_parts[0]}")

    if not found:
        print("Сьогодні ніхто з учнів не святкує день народження.")
    print()


def main():
    students = {
        "Щербань Дарія Миколаївна": (2006, 3, 30),
        "Бачиш Павло Геннадійович": (2007, 10, 21),
        "Козинець Володимир Андрійович": (2007, 6, 10),
        "Гиренко Ілля Романович": (2006, 11, 2),
        "Сагайдак Богдан Андрійович": (2007, 9, 13),
        "Мартиненко Олександр Володимирович": (2006, 5, 24),
        "Репін Данііл Вікторович": (2006, 7, 25),
        "Голишев Артем Антонович": (2007, 6, 30),
        "Шкурат Дар`я Андріївна": (2007, 11, 2),
        "Біла Єлизавета Сергіївна": (2007, 6, 11),
    }

    while True:
        print("МЕНЮ")
        print("1. Вивести повний список учнів")
        print("2. Додати нового учня")
        print("3. Видалити учня")
        print("4. Відсортувати")
        print("5. Перевірити, у кого з учнів сьогодні день народження")
        print("0. Вихід зі словника")

        choice = input("Ваш вибір: ").strip()
        print()

        if choice == "1":
            list(students)
        elif choice == "2":
            add(students)
        elif choice == "3":
            delete(students)
        elif choice == "4":
            sort(students)
        elif choice == "5":
            birthday(students)
        elif choice == "0":
            print("Вихід.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.\n")


if __name__ == "__main__":
    main()
