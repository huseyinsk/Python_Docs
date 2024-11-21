#1 ile 50 arasında bir tek bir çift 10 adet rastgele sayı giriniz
sayacx = 1
sayacy = 1
while sayacx <= 5 and sayacy <= 5 :
    x = float(input("Lütfen 1 ile 50 arasında tek sayı giriniz: "))
    if x < 1 or x > 50:
        print("Lütfen 1 ile 50 arasında tek sayı giriniz: ")
        continue
    if x %2 == 0:
        print("Lütfen bir tek sayı giriniz.")
        continue
    print("Girmiş olduğunuz sayı: ", x)
    y = float(input("Lütfen 1 ile 50 arasında çift sayı giriniz: "))
    if y < 1 or y > 50:
        print("Lütfen 1 ile 50 arasında çift sayı giriniz: ")
        continue
    if y %2 != 0:
        print("Lütfen bir çift sayı giriniz.")
        continue
    print("Girmiş olduğunuz sayı: ", y)
    sayacy += 1
    sayacx += 1
print("Bir tek bir çift toplamda 5 adet sıralı sayı girdiniz.")
#1 ile 50 arasında bir tek bir çift 10 adet rastgele sayı giriniz
