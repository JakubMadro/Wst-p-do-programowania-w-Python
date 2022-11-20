import random

zestaw_1 = []
x = int(input("Podaj Liczbe: "))

for i in range(x):
    zestaw_1.append(random.randint(1,10))

print(zestaw_1)


y = int(input("Podaj Liczbe: "))

zestaw_2 = [random.randint(5,15) for i in range(y)]

check_var = int(input("Podaj liczke jaka chcesz sprawdzic: "))
check_1 = check_var in zestaw_1
check_2 = check_var in zestaw_2

if check_1 == True and check_2 == True:
    print("Liczba z 2 zestawow ")
elif check_2 == True:
    print("Liczba z zestawu 2")
elif check_1 == True:
    print("Liczba z zestawu 1")
else:
    print("liczba z poza zakresu ")

