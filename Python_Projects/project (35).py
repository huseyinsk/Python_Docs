#Soru 4: Kullanıcıya “Türkiye’nin başkenti hangi şehirdir?”sorusunu sorsun.
#Doğru cevap verilene kadar “Yanlış cevap, tekrar deneyiniz!” uyarısını versin
#Doğru cevap verildiğinde “Tebrikler, bildiniz” yazısı gösterilsin ve döngüden çıkılsın.

x = input("Türkiyenin başkenti hangi şehirdir?: ").upper()
while x != "ANKARA":
    print("Yanlış cevap verdiniz, tekrar deneyiniz!")
    x = input("Türkiyenin başkenti hangi şehirdir?: ").upper()
    if x == "ANKARA":
        print("Tebrikler, doğru cevap verdiniz.")
        break
else:
    print("Tebrikler, doğru cevap verdiniz.")

#Soru 4: Kullanıcıya “Türkiye’nin başkenti hangi şehirdir?”sorusunu sorsun.
#Doğru cevap verilene kadar “Yanlış cevap, tekrar deneyiniz!” uyarısını versin
#Doğru cevap verildiğinde “Tebrikler, bildiniz” yazısı gösterilsin ve döngüden çıkılsın.
