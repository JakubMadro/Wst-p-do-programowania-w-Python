print('''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
Wpisz numer operacji: 
''')

mode = int(input("Podaj mode: "))
if mode > 5 or mode < 1:
    print("niepoprawne dzialanie!")
    exit()


var1 = float(input("podaj var1:"))
var2 = float(input("podaj var2:"))

if mode == 1:
    wynik = var1+var2

elif mode == 2:
    wynik = var1-var2

elif mode == 3:
    wynik = var1*var2

elif mode == 4:
    if var2 == 0:
        print("Nie mozesz dzielic przez 0:")
        exit()
    else:
        wynik = var1/var2

elif mode == 5:
    wynik == var1**var2

print("Wynik operacji", mode, "to:", wynik)






