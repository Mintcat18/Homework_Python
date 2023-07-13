'''Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S 
и их произведение P. Помогите Кате отгадать задуманные Петей числа.'''

S = int(input("сумма чисел: ")) 
P = int(input("произведение чисел: ")) 

D = S * S - 4 * P 

if D < 0: 
    print("NO")
elif D == 0: 
    X = Y = S / 2
    if X.is_integer() and Y.is_integer():
        print(int(X), int(Y))
    else:
        print("NO")
else:
    X1 = (S + D ** 0.5) / 2
    X2 = (S - D ** 0.5) / 2
    if X1.is_integer() and X1 > 0:
        print(int(X1), int(P / X1))
    elif X2.is_integer() and X2 > 0:
        print(int(X2), int(P / X2))
    else:
        print("NO")