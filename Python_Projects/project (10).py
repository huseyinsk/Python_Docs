#1 ile 50 arasında rastgele 10 adet sayı giriniz.
sayac = 0
while sayac <= 9 :
    x = float(input("1 ile 50 arasında rastgele bir sayı giriniz: "))
    if x < 1 or x > 50:
        print("Lütfen 1 ile 50 arasında rastgele bir sayı giriniz.")
        continue
    print("Girmiş olduğunuz sayı: ", x)
    sayac += 1
print("1 ile 50 arasında 10 adet rastgele sayı girdiniz.")
#1 ile 50 arasında rastgele 10 adet sayı giriniz.

