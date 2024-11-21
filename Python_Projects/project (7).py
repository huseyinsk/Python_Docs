# Kullanıcının adını doğru girebilmesi için 3 hak tanıyan döngü
x = input("Bir isim giriniz: ")
while x != "hüseyin":
    print("Hatalı isim girdiniz, 3 hakkınız kaldı.")
    x = input("bir isim giriniz: ")
    if x != "hüseyin":
        print("Hatalı isim girdiniz, 2 hakkınız kaldı.")
        x = input("Bir isim giriniz: ")
        if x!= "hüseyin":
            print("Hatalı isim girdiniz, 1 hakkınız kaldı.")
            x = input("Bir isim giriniz: ")
            if x!= "hüseyin":
                print("Hatalı isim girdiniz!")
                print("Daha sonra tekrar deneyiniz.")
                break
else:
    if x == "hüseyin":
        print("Tebrikler, doğru isim girdiniz.")
# Kullanıcının adını doğru girebilmesi için 3 hak tanıyan döngü
