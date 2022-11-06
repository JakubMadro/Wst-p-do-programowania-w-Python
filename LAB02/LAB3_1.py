var1 = int(input("Podaj wartosc 1:"))
var2 = int(input("podaj wartosc 2:"))

if var2<var1:
    (var1,var2)=(var2,var1)

while var1<=var2:
    print(var1,end=",")
    var1+=1