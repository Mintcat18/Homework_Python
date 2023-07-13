"""Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10
"""

s = int(input('Укажите количество журавликов, сделанное тремя детьми: '))

divisor = 6
if s % divisor != 0:
    print('Некорректное количество')
else:
    ab = s // 3 
    c = ab * 2 
    a = ab // 2
    b = a

    print("Петя сделал", a, "журавликов")
    print("Катя сделала", c, "журавликов")
    print("Сережа сделал", b, "журавликов")
