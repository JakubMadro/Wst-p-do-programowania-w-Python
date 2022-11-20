import random

punkty = [round(random.uniform(0,50),2) for i in range(15)]

print(punkty)

print("Minimalna ilosc punktow",min(punkty))
print("Max ilosc punktow:", max(punkty))

anv = sum(punkty) / len(punkty)
print(anv)