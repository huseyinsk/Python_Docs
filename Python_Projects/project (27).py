#ALIŞTIRMA 1:
#Yas ve isim parametreleri alan ve aşağıdaki durumlara göre
#mesajları ekrana yazan karsilama2() fonksiyonunu yazınız.

name = input("İsminizi giriniz: ")
age = int(input("Yaşınızı giriniz: "))

def function(name,age):
    """
    yaşa bağlı hitap eden fonksiyon
    """
    if age <= 10:
        print("Merhaba çocuk {}, Hoş geldin.".format(name))
    elif 10 < age and age < 30:
        print("Merhaba genç {}, Hoş geldin.".format(name))
    else:
        print("Merhaba efendim {}, Hoş geldin.".format(name))

function(name,age)


#ALIŞTIRMA 1:
#Yas ve isim parametreleri alan ve aşağıdaki durumlara göre
#mesajları ekrana yazan karsilama2() fonksiyonunu yazınız.
