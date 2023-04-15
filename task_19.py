''' На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть'''

n = int(input()) 
coins = input() 

heads = coins.count("H") 
tails = coins.count("T") 

if heads > tails:
    flipped = coins.replace("T", "H") 
    flips = tails 
else:
    flipped = coins.replace("H", "T") 
    flips = heads 

print(flips) 