#Soru 1: Bir sayı dizisinin ortalamasını hesaplayan bir programımız var. Sizden bir sayı girmenizi ve ardından isterseniz başka bir sayı daha
#girmenizi isteyeceğiz. Sayı girişlerinizi bitirmek ve ortalamayı hesaplamak istediğinizde, programın size soracağı "Çıkmak ister misiniz?"
#sorusuna "Evet" yanıtını vermeniz yeterli. Eğer devam etmek istiyorsanız "Hayır" demeniz ve ardından yeni sayınızı girmeniz beklenir.

sayac = 1
y = 0
while sayac > 0 :
    x = float(input("Bir sayı giriniz: "))
    y += x
    ortalama = y / sayac
    sayac += 1
    a = input("Çıkmak ister misiniz?: ").lower()
    if a == "evet":
        print("Girdiğiniz değer ortalaması: ", ortalama)
        break
    elif a == "hayır":
        continue
    else:
        print('Lütfen çıkmak istediğinizi "Evet" veya "Hayır" olarak belirtiniz. Tekrar deneyiniz!')
        b = input("Çıkmak ister misiniz?: ").lower()
        if b == "hayır":
            continue
        elif b == "evet":
            print("Girdiğiniz değer ortalaması: ", ortalama)
            break
        else:
            print("ERROR 404, Sonra tekrar deneyiniz.")
            break
else:
    print("Girdiğiniz değer ortalaması: ", ortalama)

#Soru 1: Bir sayı dizisinin ortalamasını hesaplayan bir programımız var. Sizden bir sayı girmenizi ve ardından isterseniz başka bir sayı daha
#girmenizi isteyeceğiz. Sayı girişlerinizi bitirmek ve ortalamayı hesaplamak istediğinizde, programın size soracağı "Çıkmak ister misiniz?"
#sorusuna "Evet" yanıtını vermeniz yeterli. Eğer devam etmek istiyorsanız "Hayır" demeniz ve ardından yeni sayınızı girmeniz beklenir.


