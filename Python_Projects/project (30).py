#ALIŞTIRMA 2:
#sayi isimli tek bir parametre alan ve girilen sayinin faktöriyelini bulup,aşağıdaki
#ekran çıktısı şeklinde ekrana yazan faktoriyel() fonksiyonunu yazınız.

the_number = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz: "))

def factorial_function(the_number):
    """    
    Faktöriyel bulan fonksiyon
    """
    if the_number == 1 or the_number == 0:
        print(f"Girmiş olduğunuz {the_number} sayısının faktöriyeli: 1'dir.")
    elif the_number < 0:
        print("Lütfen bir doğal sayı giriniz.")
    else:
        factorial = 1
        for i in range(1, the_number + 1):
            factorial *= i
        print(f"Girmiş olduğunuz {the_number} sayısının faktöriyeli: ", factorial)

factorial_function(the_number)        

#ALIŞTIRMA 2:
#sayi isimli tek bir parametre alan ve girilen sayinin faktöriyelini bulup,aşağıdaki
#ekran çıktısı şeklinde ekrana yazan faktoriyel() fonksiyonunu yazınız.
