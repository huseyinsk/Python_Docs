#Fibonacci dizisini verilen terime kadar bulunuz.
f0 = 0
f1 = 1
f2 = f1 + f0
fn = fn-1 + fn-2
n = 0
list = []
TerSay = int(input("Terim sayısını giriniz: "))
while n <= TerSay:
    fn = fn-1+fn-2
    n+=1
print(TerSay)
