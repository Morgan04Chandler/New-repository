import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('comptagevelo2012.csv')

print(df.head())
print(df.info())
print(df.describe())

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y') # колонку date переводимо у потрібний формат

# загальна кількість велосипедистів за рік на усіх велодоріжках
# Спочатку обираємо потрібні колонки з велодоріжками
bike_columns = df.columns[2:]  # оскільки перші дві колонки це date та порожня

total_year = df[bike_columns].sum().sum()
print(f"Загальна кількість велосипедистів за рік на усіх велодоріжках: {total_year}")

# загальна кількість велосипедистів за рік на кожній велодоріжці
total_per_track = df[bike_columns].sum()
print("\nЗагальна кількість велосипедистів за рік на кожній велодоріжці:")
print(total_per_track)

df['Month'] = df['Date'].dt.month

month_names = { # створимо словник щоб номер місяця був буквами
    1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень',
    5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень',
    9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'
}

user_input = input("Введіть назви велодоріжок через кому: ")
tracks = [track.strip() for track in user_input.split(',')] # розділяємо введений рядок по комі та видаляємо зайві пробіли

popular_months = {} # створюємо словник для зберігання місяця найбільшої популярності кожної велодоріжки
for track in tracks:
    if track in df.columns:
        monthly_sum = df.groupby('Month')[track].sum() # групуємо дані по місяцях та підсумовуємо кількість по кожній велодоріжці
        most_popular_month_num = monthly_sum.idxmax() # знаходимо номер найпопулярнішого місяцю
        popular_months[track] = month_names[most_popular_month_num] # перетворюємо номер місяця у буквений формат і додаємо до словника
    else:
        popular_months[track] = 'Невідома велодоріжка'

print("\nМісяць найбільшої популярності на обраних велодоріжках:")
for track, month in popular_months.items():
    print(f"{track}: {month}")

# побудова графіку завантаженості однієї з велодоріжок по місяцям
track_name = input("Введіть назву велодоріжки для графіку: ")

monthly_data = df.groupby('Month')[track_name].sum()# групуємо дані по місяцях та підсумовуємо кількість по кожному місяцю

plt.figure(figsize=(10, 6))
monthly_data.plot(kind='bar', color='skyblue')
plt.title(f"Завантаженість велодоріжки {track_name} по місяцям за 2012 рік")
plt.xlabel("Місяць")
plt.ylabel("К-сть велосипедистів")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()
