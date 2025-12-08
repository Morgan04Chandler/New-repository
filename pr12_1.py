import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def data(file_name):
    try:
        df = pd.read_csv(file_name)
        return df
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return None

def peredobrobka(df):
    df = df.dropna()
    if df.shape[1] < 2: # стовпців має бути хоча б 2, тобто х та у
        print("Недостатньо стовпців у файлі для обробки.")
        return None, None
    x = df.iloc[:, 0].to_numpy()
    y = df.iloc[:, 1].to_numpy()
    return x, y

def model(x, A, x0, B):
    # функція f(x) = A / (1 + exp(-(x - x0)/B)).
    return A / (1 + np.exp(-(x - x0) / B))

def logistic(x, y):
    # підбираэмо параметри логістичної моделі за методом найменших квадратів
    p0 = [max(y), np.median(x), 1.0] # початкові наближення: max y, медіана x, B=1
    try:
        popt, _ = curve_fit(model, x, y, p0=p0)
        return popt
    except Exception as e:
        print(f"Не вдалося знайти параметри логістичної моделі: {e}")
        return None

def polynomial(x, y, degree=2):
    # підбираємо коефіцієнти полінома заданого степеня
    try:
        coefs = np.polyfit(x, y, degree)
        return coefs
    except Exception as e:
        print(f"Не вдалося знайти поліноміальні коефіцієнти: {e}")
        return None

def results(x, y, x_line, y_line, model_name):
    # будуємо графік вихідних даних та апроксимаційної кривої
    plt.figure(figsize=(9,6))
    plt.scatter(x, y, color='blue', label='Дані')
    plt.plot(x_line, y_line, color='red', label='Апроксимація')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Апроксимація ({model_name})')
    plt.legend()
    plt.tight_layout()
    plt.savefig('graphic.png')
    plt.show()
    plt.close()
    print("Графік збережено у файл 'graphic.png'.")

def main():
    file_name = input("Введіть назву CSV-файлу з даними: ")
    df = data(file_name)
    if df is None:
        return

    x, y = peredobrobka(df)
    if x is None or y is None:
        return

    while True:
        choice = input("Оберіть модель розв'язання(1 - логістична, 2 - поліноміальна) або 0, щоб завершити: ")
        if choice == '1': # логістична апроксимація
            popt = logistic(x, y)
            if popt is None:
                return
            A_fit, x0_fit, B_fit = popt
            print(f"Отримані параметри логістичної моделі: A={A_fit:.4f}, x0={x0_fit:.4f}, B={B_fit:.4f}")
            # створення точок для графіка
            x_line = np.linspace(min(x), max(x), 100)
            y_line = model(x_line, A_fit, x0_fit, B_fit)
            model_name = "Логістична"
            parametry_df = pd.DataFrame({
                'Параметр': ['A', 'x0', 'B'],
                'Значення': [A_fit, x0_fit, B_fit]
            })
        elif choice == '2': # поліноміальна апроксимація
            degree = 2
            coefs = polynomial(x, y, degree)
            if coefs is None:
                return
            print(f"Отримані коефіцієнти полінома: {coefs}")
            x_line = np.linspace(min(x), max(x), 100)
            y_line = np.polyval(coefs, x_line)
            model_name = f"Поліноміальна(Степінь={degree})"
            parametry_df = pd.DataFrame({
                'Коефіцієнт': [f'a{i}' for i in range(len(coefs)-1, -1, -1)],
                'Значення': coefs[::-1]  # [a0, a1, ...] в порядку зростання степеня
            })
        elif choice == '0':
            print("Вихід.")
            break
        else:
            print("Оберіть модель одну з двох на вибір.")
            continue

        results(x, y, x_line, y_line, model_name)

        parametry_df.to_csv('results.csv', index=False)
        print("Параметри моделі збережено у файл 'results.csv'.")

if __name__ == "__main__":
    main()