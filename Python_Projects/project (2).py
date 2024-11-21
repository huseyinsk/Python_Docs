sayi = int(input("Çalışanın yıl sonu puanı: "))
zam_orani = 0
zam_orani1 = 0.1
zam_orani2 = 0.2
zam_orani3 = 0.3
para = 2000
if sayi in (0 , 1 , 2) :
    print("Zam oranı: 0    Zam miktarı: ", zam_orani*para)
elif sayi in (3, 4, 5) :
    print("Zam oranı: 0.1    Zam miktarı: ", zam_orani1*para)
elif sayi in (6, 7, 8) :
    print("Zam oranı: 0.2    Zam miktarı: ", zam_orani2*para)
elif sayi in (9, 10) :
    print("Zam oranı: 0.3    Zam miktarı: ", zam_orani3*para)
else:
    print("Lütfen 0-10 arasında puan giriniz.")
