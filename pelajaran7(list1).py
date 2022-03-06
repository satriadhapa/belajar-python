# python liss

# list
mylist = ["aku", 1, 3,"kau","lol", "cinta"]
print(mylist)

# cara untuk menghitung panjang list

print(len(mylist))

# list dapat diisi dengan beberapa type data

mylist1 = ["aku", "sayang", "kamu"]
mylist2 = [1, 2, 3, 4, 5]
mylist3 = [True, True, False]

# kita dapat memasukan berbagai macam type data dalam 1 list

mylist4 = ["apel", "pisang", "ceri"]
print(type(mylist4))

# cara untuk mengakses list sesuai index
print(mylist[1])

# cara mengakses list dari belakang atau negatif 
print(mylist[-1])

# mengakses list dengan spesifik index
print(mylist[2:4])

# cara mengakses list dari awal sampe index ke-
print(mylist[:4])

# cara mengakses list dari index ke- sampai akhir
print(mylist[2:])

# cara mengakses list dengan negatif index
print(mylist[-2:-4])

# cara untuk mengecek ada atau tidak index dalam suatu list
if 2 in mylist:
    print("betul ada")
else:
    print("tidak ada")
    
# cara untuk mengganti item dalam sebuah list
mylist[2] = "satria"
print(mylist)

# mengganti list dalam bentuk range
mylist[2:3] = ["jojo", 5]
print(mylist)

# cara mengganti isi dalam list sesuai indeks ke berapa yang diinginkan

mylist2 = [1, 2, 4, 2,5]
mylist2[1:2] = ["satria"]
print(mylist2)

# cara memasukkan value list baru kedalam sebuah list yang sudah ada

mylist2.insert(3, "jajangmeong")
print(mylist2)

# cara menambahkan value list ke antrian akhir list

mylist2.append("mie korea")
print(mylist2)

# cara menambahkan list baru kedalam sebuah list atau memperpanjang list
# bisa juga di sebut menyatukan 2 list

mylist3 = [1, 5, "aku", 0, 2]
mylist2.extend(mylist3)

print(mylist2,"\n","panjang list = ",len(mylist2))

# cara untuk menyatukan list dengan tuple atau type data lain diinginkan
mytuple = ("1", 2, 4, "aku")
mylist2.extend(mytuple)
print(mylist2)

# cara untuk menghapus value dalam sebuah list
mylist2.remove("satria")
print(mylist2)

# cara menghapus value dalam list dengan detail sesuai pemanggilan indeks
mylist2.pop(4)
print(mylist2)

del mylist2[5]
print(mylist2)

# jika tidak ingin menghapus sesuai spesifik indek cukup jangan masukkan parameter dalam fungsi pop
mylist2.pop()
print(mylist2) # ini akan menghapus value list yang terakhir

# jika ingin menghapus semua list cukup gunakan fungsi del

## del mylist2
print(mylist2) # output list tidak akan di temukan

# cara membersihkan isi list
## mylist2.clear()
print(mylist2)


