#Soru 3:Kullanıcı tarafından klavyeden girilen bir sayının asal sayı olup
#olmadığını kontrol edip, ekrana yazan Python programını yazınız.

x = int(input("Bir sayı giriniz: "))
y = 1
sayac = 0
while y <= x:
    if x % y == 0:
        sayac += 1
    y += 1
if sayac == 2:
    print(f"Girdiğiniz {x} sayısı bir asal sayıdır.")
elif x < 0:
    print("Lütfen bir doğal sayı giriniz.")
else:
    print(f"Girdiğiniz {x} sayısı bir asal sayı değildir.")


#Soru 3:Kullanıcı tarafından klavyeden girilen bir sayının asal sayı olup
#olmadığını kontrol edip, ekrana yazan Python programını yazınız.
