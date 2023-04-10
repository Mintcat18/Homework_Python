"""Задача No11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6"""

A = int(input("Введите число: "))
fib1 = 1
fib2 = 1
i = 3
if A == fib1: print("№1")
while A >= i:
    fibsum = fib1 + fib2
    fib1 = fib2
    fib2 = fibsum
    if fibsum == A:
        print(f"№{i}")
        break
    elif A < fibsum:
        print("-1")
        break
    else: i += 1