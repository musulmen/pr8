while True:
    inp = input("Введите число (или 'stop'/'end' для выхода): ")

    if inp.lower() in ['stop', 'end']:
        break

    try:
        num = float(inp)
        print(f"Вы ввели  {num}")
    except ValueError:
        print("Ошибка: введите корректное число.")