import math


def tabulate_function():
    print("=" * 45)
    print(" Лабораторна робота: Табулювання функції y = sin(x) + 1 ")
    print("=" * 45)

    try:

        a = float(input("Введіть ліву межу (a): "))
        b = float(input("Введіть праву межу (b): "))
        h = float(input("Введіть крок (h): "))


        if h <= 0:
            raise ValueError("Крок (h) повинен бути більшим за нуль.")
        if a > b:
            raise ValueError("Ліва межа (a) не може бути більшою за праву (b).")


        to_screen = input("Виводити результати на екран? (так/ні): ").strip().lower() != 'ні'
        to_file = input("Зберігати результати у файл? (так/ні): ").strip().lower() == 'так'
        to_array = input("Зберігати результати в масив (список)? (так/ні): ").strip().lower() == 'так'

        x = a
        results_array = []
        file_content = []

        header = "X\t\tY"
        file_content.append(header)

        if to_screen:
            print("\n" + header)
            print("-" * 25)


        max_val = math.sin(a) + 1
        min_val = max_val
        count_filtered = 0


        while x <= b + h / 2:
            y = math.sin(x) + 1

            if to_screen:
                print(f"{x:.2f}\t\t{y:.2f}")

            file_content.append(f"{x:.2f}\t{y:.2f}")

            if to_array:
                results_array.append((round(x, 2), round(y, 2)))


            if y > max_val:
                max_val = y
            if y < min_val:
                min_val = y


            if 0.5 < y < 1:
                count_filtered += 1

            x += h


        print("-" * 25)
        print(f"Максимальне значення функції (max): {max_val:.4f}")
        print(f"Мінімальне значення функції (min): {min_val:.4f}")
        print(f"Кількість значень y (в діапазоні від 0.5 до 1): {count_filtered}")


        if to_file:
            filename = input("Введіть назву файлу (наприклад, results.txt): ").strip()
            if not filename:
                filename = "results.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("\n".join(file_content))
            print(f"[Успіх] Результати записано у файл '{filename}'.")


        if to_array:
            print(f"\nСтворений масив даних: {results_array}")

    except ValueError as err:

        print(f"\n[ПОМИЛКА] Помилка введення даних: {err}")
    except Exception as err:

        print(f"\n[ПОМИЛКА] Сталася непередбачена помилка: {err}")


if __name__ == "__main__":
    while True:
        tabulate_function()
        repeat = input("\nБажаєте повторити виконання програми? (так/ні): ").strip().lower()
        if repeat != 'так':
            print("Роботу програми завершено. До побачення!")
            break