#Latihan 2 Mencari bilangan terbesar dari n buah data yang di inputkan
#Contoh 1
a = int(input("Masukkan Bilangan a: "))
b = int(input("Masukkan Bilangan b: "))
c = int(input("Masukkan Bilangan c: "))
d = int(input("Masukkan Bilangan d: "))
e = int(input("Masukkan Bilangan e: "))
f = int(input("Masukkan Bilangan f: "))

if a>b and a>c and a>d and a>e and a>f:
    print("Bilangan Terbesar = ",a)
if b>a and b>c and b>d and b>e and b>f:
    print("Bilangan Terbesar = ",b)
if c>a and c>b and c>d and c>e and c>f:
    print("Bilangan Terbesar = ",c)
if d>a and d>b and d>c and d>e and d>f:
    print("Bilangan Terbesar = ",d)
if e>a and e>b and e>c and e>d and e>f:
    print("Bilangan Terbesar = ",e)
if f>a and f>b and f>c and f>d and f>e:
    print("Bilangan Terbesar = ",f)

#Contoh 2
#Latihan 2 contoh ke 2
print("Program menampilkan bilangan terbesar dari n bilangan")

a = 1
max = 0
while a !=0:
    if a > max:
        max = a
    a = int(input("Masukkan bilangan:"))
    if a == 0:
        break
print("Nilai terbesar adalah:", max)