kenar1 = int(input("Bir kenar uzunluğu giriniz."))
kenar2 = int(input("Bir kenar uzunluğu giriniz."))
kenar3 = int(input("Bir kenar uzunluğu giriniz."))

if kenar1 == kenar2 == kenar3 :
    print("Üçgenin türü eşitkenar üçgendir.")
elif kenar1 == kenar2 != kenar3 :
    print("Üçgenin türü ikizkenar üçgendir.")
elif kenar1 != kenar2 == kenar3 :
    print("Üçgenin türü ikizkenar üçgendir.")
elif kenar1 == kenar3 != kenar2 :
    print("Üçgenin türü ikizkenar üçgendir.")
else:
    print("Üçgenin türü çeşitkenar üçgendir.")
