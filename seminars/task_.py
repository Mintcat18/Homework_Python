#Напечатать двухзначные числа кратные 4, но не кратные 6

i = 10
while 100 > i:
    if i%4 == 0 and i%6 != 0:
        print(i,end=" ")
    i+=1