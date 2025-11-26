import nltk
import matplotlib.pyplot as plt
import string
from collections import Counter
from nltk.corpus import stopwords

nltk.download('stopwords')

with open('bible-kjv.txt', 'r', encoding='utf-8') as file:
    text = file.read()

def process_text(text, remove_stopwords=True): # оброблюємо текст
    text = text.lower() # та перетворюємо до нижнього регістру

    text = text.translate(str.maketrans('', '', string.punctuation + string.digits)) # видаляємо пунктуацію/цифри

    words = text.split() # та розділяємо на слова

    if remove_stopwords: # видаляємо стоп-слова
        stop_words = set(stopwords.words('english'))
        # додаємо додаткові стоп-слова для видалення
        additional_stopwords = {'thou', 'thee', 'thy', 'thine', 'ye', 'shall', 'unto', 'upon', 'thus', 'lo'}
        stop_words.update(additional_stopwords)
        words = [word for word in words if word not in stop_words and len(word) > 1]

    return words

all_words = process_text(text, remove_stopwords=False) # визначаємо к-сть слів
print(f"Загальна кількість слів у тексті: {len(all_words)}")

word_counts_with_stopwords = Counter(all_words)
top_10_with_stopwords = word_counts_with_stopwords.most_common(10) # визначаємо 10 найбільш вживаних слів

print("\n10 найбільш вживаних слів, включно зі стоп-словами:")
for i, (word, count) in enumerate(top_10_with_stopwords, 1):
    print(f"{i}. {word}: {count}")

# будуємо діаграму
words, counts = zip(*top_10_with_stopwords)
plt.figure(figsize=(12, 6))
bars = plt.bar(words, counts, color='skyblue', alpha=0.7)
plt.title('10 найбільш вживаних слів, включно зі стоп-словами', fontsize=14)
plt.xlabel('Слова', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.xticks(rotation=45, ha='right')

for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
             str(count), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# видаляємо стоп-слова та повторюємо пошук ще раз
filtered_words = process_text(text, remove_stopwords=True)
print(f"\nКількість слів після видалення стоп-слів: {len(filtered_words)}")

word_counts_filtered = Counter(filtered_words)
top_10_filtered = word_counts_filtered.most_common(10)

print("\n10 найбільш вживаних слів, без стоп-слів та пунктуації:")
for i, (word, count) in enumerate(top_10_filtered, 1):
    print(f"{i}. {word}: {count}")

# будуємо другу діаграму
words_filtered, counts_filtered = zip(*top_10_filtered)
plt.figure(figsize=(12, 6))
bars_filtered = plt.bar(words_filtered, counts_filtered, color='lightcoral', alpha=0.7)
plt.title('10 найбільш вживаних слів, без стоп-слів та пунктуації', fontsize=14)
plt.xlabel('Слова', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.xticks(rotation=45, ha='right')

for bar, count in zip(bars_filtered, counts_filtered):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
             str(count), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# додаткові розрахунки
print(f"\nДодаткові відомості:")
print(f"Загальна кількість унікальних слів: {len(set(all_words))}")
print(f"Кількість унікальних слів після фільтрації: {len(set(filtered_words))}")
print(f"Відсоток слів, що залишилися після фільтрації: {len(filtered_words) / len(all_words) * 100:.1f}%")
punctuation_count = sum(1 for char in text if char in string.punctuation) # аналізуємо пунктуацію
print(f"Кількість розділових знаків у тексті: {punctuation_count}")

# приклади видалених стоп-слів
stop_words = set(stopwords.words('english'))
additional_stopwords = {'thou', 'thee', 'thy', 'thine', 'ye', 'shall', 'unto', 'upon', 'thus', 'lo',}
all_stopwords = stop_words.union(additional_stopwords)

# знайдемо найбільш вживані стоп-слова
stopwords_in_text = {word: count for word, count in word_counts_with_stopwords.items()
                     if word in all_stopwords and count > 100}
top_stopwords = sorted(stopwords_in_text.items(), key=lambda x: x[1], reverse=True)[:10]