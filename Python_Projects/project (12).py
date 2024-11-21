#Soru 2: Bir hayvanat bahçesinin fiyatlandırma politikası, ziyaretçilerin yaş gruplarına göre değişiklik göstermektedir
#ve sizden, bir Python, programı yazarak bu politikanın uygulanmasını otomatize etmenizi istiyoruz.

kisiler = int(input("Grup içinde kaç kişi var ?: "))
ucret = 0

for grup in range(kisiler):
    x = int(input(f"{grup + 1}. kişinin yaşı nedir ?: "))
    if x <= 2:
        print("Giriş ücretsizdir.")
        continue
    elif x >= 3 and x <= 12:
        print("Giriş ücreti, 14 TL'dir.")
        ucret +=14
    elif x >= 65:
        print("Giriş ücreti , 18 TL'dir.")
        ucret += 18
    else:
        print("Giriş ücreti, 23 TL'dir.")
        ucret += 23
print("Toplam ücret bedeliniz: ", ucret)

#Soru 2: Bir hayvanat bahçesinin fiyatlandırma politikası, ziyaretçilerin yaş gruplarına göre değişiklik göstermektedir
#ve sizden, bir Python, programı yazarak bu politikanın uygulanmasını otomatize etmenizi istiyoruz.


