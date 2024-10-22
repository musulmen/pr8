import os
import time

def set_cursor(x, y):
    print(f"\033[{y};{x}H", end='')

def draw_square():
    size = 10
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                set_cursor(j + 1, i + 1)
                print('*', end='')
            else:
                set_cursor(j + 1, i + 1)
                print(' ', end='')
        print()

    time.sleep(0.1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    draw_square()
    time.sleep(1)