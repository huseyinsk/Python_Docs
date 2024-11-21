#Bir sayının asal sayı olup olmadığını kontrol eden program:

CheckNum = int(input("Kontrol etmek istediğiniz sayıyı giriniz: "))
if CheckNum == 1:
    print("Bir sayısı bir asal sayı değildir.")
elif CheckNum < 0:
    print("Lütfen bir doğal sayı giriniz:")
elif CheckNum == 2:
    print("Girmiş olduğunuz 2 sayısı bir asal sayıdır.")
else:
    for till in range(2,CheckNum):
        if CheckNum % till == 0:
            print(f"Girmiş olduğunuz {CheckNum} sayısı bir asal değildir")
            break
    else:
        print(f"Girmiş olduğunuz {CheckNum} sayısı bir asal sayıdır.")

