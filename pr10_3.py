import json
import matplotlib.pyplot as plt
from collections import Counter  # використаємо для підрахунку елементів

def create():
    try:
        with open('students_add.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        print("Файл успішно завантажено.")

    except FileNotFoundError:
        print("Файл students_add.json не знайдено.")
        return

    except json.JSONDecodeError:
        print("Файл students_add.json має неправильний формат JSON.")
        return

    # створимо список для дод.занять
    additional_lessons = []

    for student in data:
        # проходимо по кожному студенту та перевіряємо чи є у нього add.lesson
        if "Additional lesson" in student:
            additional_lessons.append(student["Additional lesson"])
        else:
            print(f"Студент {student.get('Surname', 'Невідомо')} не має додаткового заняття")

    if not additional_lessons: # помилка при відсутності даних для діаграми
        print("Немає даних про додаткові заняття для побудови діаграми.")
        return

    lesson_counts = Counter(additional_lessons)

    labels = list(lesson_counts.keys())

    sizes = list(lesson_counts.values())

    total = sum(sizes)

    percentages = [f'{(size / total) * 100:.1f}%' for size in sizes]

    plt.figure(figsize=(12, 9))

    # використаємо палітру кольорів Set3 що вже є в matplotlib
    colors = plt.cm.Set3(range(len(labels))) # таким чином отримаємо різні кольори

    wedges, texts, autotexts = plt.pie(sizes, labels=labels,
        colors=colors, autopct='%1.1f%%',
        startangle=90, textprops={'fontsize': 12}
    )

    plt.title(
        'Розподіл студентів за додатковими заняттями', fontsize=16,
        fontweight='bold', pad=20
    )

    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(12)

    for text in texts:
        text.set_fontsize(12)

    plt.legend(
        wedges,
        [f'{label}: {count} студ.' for label, count in zip(labels, sizes)],
        title="Додаткові заняття",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1)
    )

    plt.axis('equal')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    create()