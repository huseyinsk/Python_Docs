#ALIŞTIRMA 4:
#Hiçbir parametre almayan ve kullanıcıdan üç sayı girmesini isteyen ve
#sonuç olarak bu değerlerin medyan değerini veren bir fonksiyon yazınız.

first_number = float(input("Birinci sayıyı giriniz: "))
second_number = float(input("İkinci sayıyı giriniz: "))
third_number = float(input("Üçüncü sayıyı giriniz: "))

def median_function ():
    """
    medyanı veren fonksiyon
    """
    the_list = [first_number , second_number , third_number]
    the_list.sort()
    print("Girilen sayının medyanı: ", the_list[1])

median_function()

#ALIŞTIRMA 4:
#Hiçbir parametre almayan ve kullanıcıdan üç sayı girmesini isteyen ve
#sonuç olarak bu değerlerin medyan değerini veren bir fonksiyon yazınız.    

