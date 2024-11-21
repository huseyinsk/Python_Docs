#Aşağıdaki Akış şeması ne yapmaktadır? Kısaca belirtip Python kodunu while döngüsü kullanarak yazınız.


#Akış diyagramını görsel olarak eklemeye çalıştım ancak beceremedim.Diyagram bize sayac ve toplam değişkenlerini
#vermekte, sayaç 100 den küçük oldugu durumlarda toplam değişkenimizi her seferde üstüne ekleyecek şekilde sayaçla
#toplamakta. Sayaç 100'e eşit veya büyük oldugunda döngüden çıkacak ve toplam değişkeninin aldığı toplam değeri çıktı
#olarak verecektir.İşlem burda bize 0 dan 100 e kadar olan tek sayıların toplamını verir.


sayac = 1
toplam = 0

while sayac < 100:
    toplam += sayac
    sayac += 2

print(toplam)


#Aşağıdaki Akış şeması ne yapmaktadır? Kısaca belirtip Python kodunu while döngüsü kullanarak yazınız.
