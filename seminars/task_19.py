# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_a = [1, 2, 3, 4, 5]
k = int(input("Введите число к: "))%len(list_a)
list_b = []
for i in range(k, len(list_a)):
    list_b.append(list_a[i])
for i in range(k):
    list_b.append(list_a[i])
print(list_b)

print(list_a[k:] + list_a[:k])

