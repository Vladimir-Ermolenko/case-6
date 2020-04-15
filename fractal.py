"""Case-study
Developers:
Sharkov (65%), Ermolenko (35%)
"""

from turtle import *

def koch(order, size):
    if order == 0:
        forward(size)
    else:
        koch(order - 1, size / 3)  # Кривая Коха
        left(60)
        koch(order - 1, size / 3)
        right(120)
        koch(order - 1, size / 3)
        left(60)
        koch(order - 1, size / 3)


def snegkoch(order, size):
    koch(order, size)              # Снежинка Коха
    right(120)
    koch(order, size)
    right(120)
    koch(order, size)
    right(120)


def ice1(order, size):
    if order == 0:
        forward(size)             # Ледяной фрактал(1)
    else:
        ice1(order - 1, size / 2)
        left(120)
        ice1(order - 1, size / 4)
        right(180)
        ice1(order - 1, size / 4)
        left(120)
        ice1(order - 1, size / 4)
        right(180)
        ice1(order - 1, size / 4)
        left(120)
        ice1(order - 1, size / 2)


def ice2(order, size):
    if order == 0:
        forward(size)
    else:
        ice2(order - 1, size / 2)      # Ледяной фрактал(1)
        left(90)
        ice2(order - 1, size / 4)
        right(180)
        ice2(order - 1, size / 4)
        left(90)
        ice2(order - 1, size / 2)


def snegice1(order, size):
    ice1(order, size)                  # Снежинка к л.ф.(1)
    right(120)
    ice1(order, size)
    right(120)
    ice1(order, size)
    right(180)
    ice1(order, size)
    left(120)
    ice1(order, size)
    left(120)
    ice1(order, size)


def snegice2(order, size):
    ice2(order, size)                   # Снежинка к л.ф.(2)
    right(90)
    ice2(order, size)
    right(90)
    ice2(order, size)
    right(90)
    ice2(order, size)
    right(180)
    ice2(order, size)
    left(90)
    ice2(order, size)
    left(90)
    ice2(order, size)
    left(90)
    ice2(order, size)


def mink(order, size):
    if order == 0:
        forward(size)                    # Кривая Минковского
    else:
        mink(order - 1, size / 4)
        left(90)
        mink(order - 1, size / 4)
        right(90)
        mink(order - 1, size / 4)
        right(90)
        mink(order - 1, size / 4)
        mink(order - 1, size / 4)
        left(90)
        mink(order - 1, size / 4)
        left(90)
        mink(order - 1, size / 4)
        right(90)
        mink(order - 1, size / 4)


def levi(order, size):
    if order == 0:
        forward(size)
    else:
        left(45)
        levi(order - 1, size / 2)           # Кривая Леви
        right(90)
        levi(order - 1, size / 2)
        left(45)


def tree(order, size):
    if order == 0:
        forward(size)                       # Двоичное дерево
    else:
        tree(order - 1, size)
        right(30)
        tree(order - 1, size * 2 / 3)
        left(180)
        tree(order - 1, size * 2 / 3)
        right(120)
        tree(order - 1, size * 2 / 3)
        left(180)
        tree(order - 1, size * 2 / 3)
        right(30)
        tree(order - 1, size)
        left(180)


def main():
    up()
    goto(-100, 0)
    down()
    order = int(input('Глубина рекурсии:'))
    size = int(input('Длина стороны:'))
    fractal = int(input('1 - Кривая Коха, 2 - Снежинка Коха, 3 - Ледяной фрактал(1), 4 - Ледяной фрактал(2),'
                        '5 - Снежинка к л.ф.(1), 6 -Снежинка к л.ф.(2), 7 - Кривая Минковского,'
                        '8 - Кривая Леви, 9 - Двоичное дерево '))
    if fractal == 1:
        koch(order, size)
    elif fractal == 2:
        snegkoch(order, size)
    elif fractal == 3:
        ice1(order, size)
    elif fractal == 4:
        ice2(order, size)
    elif fractal == 5:
        snegice1(order, size)
    elif fractal == 6:
        snegice2(order, size)
    elif fractal == 7:
        mink(order, size)
    elif fractal == 8:
        levi(order, size)
    elif fractal == 9:
        tree(order, size)


main()
