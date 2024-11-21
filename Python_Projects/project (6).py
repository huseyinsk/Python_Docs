# Adını daha sonra soyadını doğru yazana kadar While döngüsünü kullanın.
x = input("Adınızı giriniz: ")
y = input("Soy adınızı giriniz: ")
while x != "hüseyin" or y != "sarıkaya":
    print("Hatalı isim veya soyisim girdiniz, lütfen tekrar deneyiniz.")
    x = input("Adınızı giriniz: ")
    if x != "hüseyin":
        while x != "hüseyin":
            print("Yanlış ad, tekrar deneyiniz!")
            x = input("Adınızı giriniz: ")
            if x == "hüseyin":
                 print("Doğru ad!")
    y = input("Soy adınızı giriniz: ")
    if y != "sarıkaya":
        while y != "sarıkaya":
            print("Yanlış soyad, tekrar deneyiniz!")
            y = input("Soy adınızı giriniz: ")
            if y == "sarıkaya":
                print("Doğru soyad!")
    if x == "hüseyin" and y == "sarıkaya":
        print("Kullanıcı doğru.")
        break
else:
    print("Kullanıcı doğru.")
# Adını daha sonra soyadını doğru yazana kadar While döngüsünü kullanın.
