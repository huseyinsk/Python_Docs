#Soru 3:Kullanıcı tarafından klavyeden girilen bir sayının asal sayı olup
#olmadığını kontrol edip, ekrana yazan Python programını yazınız.

x = int(input("Bir sayı giriniz: "))
if x == 2:
    print("Girmiş olduğunuz 2 sayısı, bir asal sayıdır.")
elif x == 0 or x == 1:
    print(f"Girmiş olduğunuz {x} sayısı, bir asal sayı değildir.")
elif x < 0:
    print("Lütfen bir doğal sayı giriniz.")
else:
    for i in range(2,(x+1)):
        if (x % i) == 0:
            print(f"{x} sayısı, bir asal sayı değildir.")
            break
        else:
            print(f"{x} sayısı, bir asal sayıdır.")
            break

#Soru 3:Kullanıcı tarafından klavyeden girilen bir sayının asal sayı olup
#olmadığını kontrol edip, ekrana yazan Python programını yazınız.
