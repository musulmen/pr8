while True:
    try:
        a = input("Введите первое число: ")
        b = input("Введите второе число: ")

        if not a.isdigit() or not b.isdigit():
            raise ValueError

        a = int(a)
        b = int(b)

        print(f"Сумма: {a + b}")

    except ValueError:
        print("Ошибка: введите два целых числа.")
