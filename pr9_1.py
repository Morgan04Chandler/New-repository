import csv

filename = "Data.csv"

try:
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        gdp_row = None
        for row in reader:
            if row["Series Name"] == "GDP per capita (current US$)" and row["Country Name"] == "Ukraine":
                gdp_row = row
                break

        if gdp_row is None:
            print("Дані для не знайдено.")
            exit()

        print("GDP per capita (current US$) - для України за 1991–2019 роки:\n")

        values = {}

        for year in range(1991, 2019 + 1):
            key = f"{year} [YR{year}]"
            value = gdp_row[key]

            if value.strip() == "":
                continue

            value = float(value)
            values[year] = value
            print(f"{year}: {value}")

        min_year = min(values, key=values.get) #шукаємо найнижче та найвище значення
        max_year = max(values, key=values.get)

        print("\nРезультати пошуку:")
        print(f"Найнижчий показник ВВП на душу населення: {min_year}: {values[min_year]}")
        print(f"Найвищий показник ВВП на душу населення: {max_year}: {values[max_year]}")

        with open("Result.csv", "w", newline="") as outfile:
            writer = csv.writer(outfile, delimiter=";")
            writer.writerow(["Type", "Year", "Value"])
            writer.writerow(["MIN", min_year, values[min_year]])
            writer.writerow(["MAX", max_year, values[max_year]])

        print("\nРезультати пошуку записано у файл Result.csv")

except FileNotFoundError:
    print("Файл Data.csv не знайдено.")