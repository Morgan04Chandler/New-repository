import csv
import matplotlib.pyplot as plt

filename = "energy.csv"

years = []
ukraine_values = []
usa_values = []

with open(filename, "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    header = next(reader)

    years = [col.split()[0] for col in header[4:]] # формуємо список років за принципом
                                                   # "2000 [YR2000]" буде "2000"

    for row in reader:
        if len(row) < 5:
            continue

        country = row[2]

        if country == "Ukraine":
            ukraine_energy = [float(x) for x in row[4:]]

        if country == "United States":
            usa_energy = [float(x) for x in row[4:]]

plt.figure(figsize=(14, 7))

plt.plot(years, ukraine_energy, marker='o', linestyle='-', linewidth=2,
         label="Україна")
plt.plot(years, usa_energy, marker='s', linestyle='-', linewidth=2,
         label="США")

plt.xlabel("Рік")
plt.ylabel("Відсоток, %")
plt.title("Renewable energy consumption (% of total final energy consumption) - Україна та США")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


data_dict = {
    "Україна": ukraine_energy,
    "США": usa_energy,
}

country_input = input("Введіть назву країни (Україна або США): ").strip()

if country_input in data_dict:
    plt.figure(figsize=(14, 7))
    plt.bar(years, data_dict[country_input])

    plt.xlabel("Рік")
    plt.ylabel("Відсоток, %")
    plt.title(f"Renewable energy consumption (% of total final energy consumption) - {country_input}")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Такої країни немає в даних.")