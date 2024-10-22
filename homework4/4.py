while True:
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))

        start = int(a) + 1 if a < b else int(b) + 1
        end = int(b) if a < b else int(a)

        for num in range(start, end):
            print(num)

    except ValueError:
        print("Ошибка: вводите только числа.")
        continue

    break