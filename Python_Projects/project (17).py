#Aritmetik dizilerin temel bir konseptini inceleyeceğimiz bir uygulama yapacaksınız. Aritmetik dizi, her terimin bir öncekinesabit bir
#fark eklenerek oluşturulduğu bir sayı dizisidir. Örneğin, 1'den başlayarak her seferinde 1 artırarak devam eden bir dizi aritmetiktir.
#Bu sorudaki göreviniz, 1'den başlayıp klavyeden girilen bir sayıya kadar olan tüm tam sayıların toplamını hesaplayacak bir Python programı
#yazmak olacak. Örneğin, eğer 6 girilirse, programınız 1+2+3+4+5+6'nın toplamını hesaplayıp ekrana yazdıracaktır.

toplam = 0
x = int(input("Bir sayı giriniz: "))
for y in range(1,(x+1),1):
    toplam += y
print("Girmiş olduğunuz sayının aritmetik dizi toplamı: ", toplam)

#Aritmetik dizilerin temel bir konseptini inceleyeceğimiz bir uygulama yapacaksınız. Aritmetik dizi, her terimin bir öncekinesabit bir
#fark eklenerek oluşturulduğu bir sayı dizisidir. Örneğin, 1'den başlayarak her seferinde 1 artırarak devam eden bir dizi aritmetiktir.
#Bu sorudaki göreviniz, 1'den başlayıp klavyeden girilen bir sayıya kadar olan tüm tam sayıların toplamını hesaplayacak bir Python programı
#yazmak olacak. Örneğin, eğer 6 girilirse, programınız 1+2+3+4+5+6'nın toplamını hesaplayıp ekrana yazdıracaktır.
