"""15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: 
арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, 
записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
Input:	5 -> 5 1 6 5 9
Output:	1 9"""

import random
n = int(input("Введите кол-во арбузов на рынке: "))
list = []
i = 0
for _ in range (n):
    list.append(random.randint(5, 20))
max = list[i]
min = list[i]
while n > i:
    if list[i] < min:
        min = list[i]
    if list[i] > max:
        max = list[i]
    i+=1
print(list)
print(f"Минимальный {min}, Максимальный {max}")