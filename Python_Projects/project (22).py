#Soru 10: Ekrana 1 tek 1 çift olmak üzere 10 tane rasgele sayı yazınız.
sayac = 0
while sayac <= 9:
    import random
    x = random.randint(1,100)
    if x %2 == 1:
        sayac += 1
        print(x)
        y = random.randint(1,100)*2
        print(y)
        sayac += 1
#Soru 10: Ekrana 1 tek 1 çift olmak üzere 10 tane rasgele sayı yazınız.
