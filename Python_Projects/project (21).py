#1 ile 50 arasında 10 adet rastgele tek sayı giriniz.
sayac = 0
while sayac <= 9:
    x = float(input("Rastgele tek sayı giriniz: "))
    if x < 1 or x > 50 :
        print("Lütfen 1 ile 50 arasında rastgele tek sayı giriniz.")
        continue
    if x %2 == 0:
        print("Lütfen tek sayı giriniz.")
        continue
    sayac += 1
    print("Girmiş olduğunuz sayı: ", x)
print("10 adet tek sayı girdiniz.")
#1 ile 50 arasında 10 adet rastgele tek sayı giriniz.
