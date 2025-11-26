import nltk
import matplotlib.pyplot as plt
import string
from collections import Counter
from nltk.corpus import stopwords

# Завантаження необхідних ресурсів NLTK
nltk.download('stopwords')

# Зчитування файлу
with open('bible-kjv.txt', 'r', encoding='utf-8') as file:
    text = file.read()


# Функція для обробки тексту
def process_text(text, remove_stopwords=True):
    # Перетворення до нижнього регістру
    text = text.lower()

    # Видалення пунктуації та цифр
    text = text.translate(str.maketrans('', '', string.punctuation + string.digits))

    # Розділення на слова
    words = text.split()

    # Видалення стоп-слів (якщо потрібно)
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        # Додаємо додаткові стоп-слова, які часто зустрічаються в біблійних текстах
        additional_stopwords = {'thou', 'thee', 'thy', 'thine', 'ye', 'hath', 'doth', 'art', 'hast', 'shall',
                                'unto', 'upon', 'thus', 'behold', 'lo', 'verily', 'saith', 'lord', 'god'}
        stop_words.update(additional_stopwords)
        words = [word for word in words if word not in stop_words and len(word) > 1]

    return words


# 1. Визначити кількість слів у тексті
all_words = process_text(text, remove_stopwords=False)
print(f"Загальна кількість слів у тексті: {len(all_words)}")

# 2. 10 найбільш вживаних слів (з стоп-словами)
word_counts_with_stopwords = Counter(all_words)
top_10_with_stopwords = word_counts_with_stopwords.most_common(10)

print("\n10 найбільш вживаних слів (з стоп-словами):")
for i, (word, count) in enumerate(top_10_with_stopwords, 1):
    print(f"{i}. {word}: {count}")

# Побудова стовпчастої діаграми (з стоп-словами)
words, counts = zip(*top_10_with_stopwords)
plt.figure(figsize=(12, 6))
bars = plt.bar(words, counts, color='skyblue', alpha=0.7)
plt.title('10 найбільш вживаних слів (з стоп-словами та пунктуацією)', fontsize=14)
plt.xlabel('Слова', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Додавання значень на стовпці
for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
             str(count), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# 3. Видалення стоп-слів та пунктуації та повторний аналіз
filtered_words = process_text(text, remove_stopwords=True)
print(f"\nКількість слів після видалення стоп-слів: {len(filtered_words)}")

word_counts_filtered = Counter(filtered_words)
top_10_filtered = word_counts_filtered.most_common(10)

print("\n10 найбільш вживаних слів (без стоп-слів та пунктуації):")
for i, (word, count) in enumerate(top_10_filtered, 1):
    print(f"{i}. {word}: {count}")

# Побудова стовпчастої діаграми (без стоп-слів)
words_filtered, counts_filtered = zip(*top_10_filtered)
plt.figure(figsize=(12, 6))
bars_filtered = plt.bar(words_filtered, counts_filtered, color='lightcoral', alpha=0.7)
plt.title('10 найбільш вживаних слів (без стоп-слів та пунктуації)', fontsize=14)
plt.xlabel('Слова', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Додавання значень на стовпці
for bar, count in zip(bars_filtered, counts_filtered):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
             str(count), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# Додаткова інформація
print(f"\nДодаткові відомості:")
print(f"Загальна кількість унікальних слів: {len(set(all_words))}")
print(f"Кількість унікальних слів після фільтрації: {len(set(filtered_words))}")
print(f"Відсоток слів, що залишилися після фільтрації: {len(filtered_words) / len(all_words) * 100:.1f}%")
punctuation_count = sum(1 for char in text if char in string.punctuation) # аналізуємо пунктуацію
print(f"Кількість розділових знаків у тексті: {punctuation_count}")

# Показати приклади видалених стоп-слів
stop_words = set(stopwords.words('english'))
additional_stopwords = {'thou', 'thee', 'thy', 'thine', 'ye', 'hath', 'doth', 'art', 'hast', 'shall',
                        'unto', 'upon', 'thus', 'behold', 'lo', 'verily', 'saith', 'lord', 'god'}
all_stopwords = stop_words.union(additional_stopwords)

# Знайти найбільш вживані стоп-слова в тексті
stopwords_in_text = {word: count for word, count in word_counts_with_stopwords.items()
                     if word in all_stopwords and count > 100}
top_stopwords = sorted(stopwords_in_text.items(), key=lambda x: x[1], reverse=True)[:10]