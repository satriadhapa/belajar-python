# python list lanjut
# loop list

# for loop

mylist1 = [1, 42, 2]
for i in mylist1:
    print(i)
print(5 * "=")
# loop dengan mengacu pada nomor indeksnya
# serta mencetak nilai sesuai panjang len diulang sebanyak panjang list

for j in range(len(mylist1)):
    print(mylist1[i])

print(5 * "=")    
# menggunakan while loop 

# diharapkan jika kita menggunakan while loop
# kita harus menentukan batas nilai yang akan di jadikan acuan
# jika tidak maka anda akan masuk ke infinite loop

k = 0
while k < len(mylist1):
    print(mylist1[k])
    k += 1

# loop dengan list comprehension yang dimana menawarkan sintaks terpendek untuk list loop

[print(x) for x in mylist1]

# membuat daftar baru list dengan for loop sesuai yang diiinginkan

mylist2 = ["apel","mangga", "anggur", "arben"]
newlist = []
for x in mylist2:
    if "a" in x:
        newlist.append(x)
print(newlist)

# cara yang lebih sederhana
newlist1 = [y for y in mylist2 if "a" in y]
print(newlist1)

# sintaks pada list comprehension
# newlist = [comprehension for item in iterable if condition == True]

# condition bisa di sebut juga sebuah filter yang dimana akan diterima jika bernilai True
# condition akan berbalik ke nilai True untuk semua element yang di sebutkan di bawah 
# dan membuat list baru tanpa menambahkan element yang sudah di sebutkan sebagai syarat tidak masuk nya element tersebut

listbaru = [m for m in mylist2 if m != "apel"]
print(listbaru)

# coba tanpa if "a"
# akan menghasilkan list yang sama dengan yang sebelumnya
listbaru2 = [n for n in mylist2]
print(listbaru2)

# iterable 
# dapat berisikan berbagai object contohnya tuple, sets, dict dan lain sebagainya

listbaru3 = [v for v in range(10)]
print(listbaru3) # output akan mengeluarkan semua nilai yang kurang dari sebuah batas yang di tentukan

# dengan condition
listbaru4 = [z for z in range(10) if z < 5]
print(listbaru4) # akan menyesuaikan dengan nilai yang di berikan pada condition

# expression
# membuat isi dalam sebuah list menjadi huruf kapital 

listbaru5 = [l.upper() for l in mylist2]
print(listbaru5)

# membuat isi dalam sebuah list menjadi huruf normal 

listbaru6 = [l.lower() for l in mylist2]
print(listbaru6)

## mengganti value dalam list dengan kata yang diiinginkan
# listbaru7 = ["hai" for l in mylist2]
# print(listbaru7)

# cara mengembalikan nilai pada sebuah list dan menimpa nilai lain

listbaru8 = [p if p != "apel" else "pisang" for p in mylist2]
print(listbaru8)

# cara mengurutkan sebuah list dengan urutan alphabet
# ascending
my_new_list = ["apel", "mangga", "jeruk", "anggur", "pisang", "markisa"]
my_new_list.sort()
print(my_new_list)

# cara mengurutkan list yang berisikan angka / int
listangka = [3, 35, 32, 53 ,53, 2, 4]
listangka.sort()
print(listangka)

# descending
listangka.sort(reverse= True)
print(listangka)

# menyesuaikan fungsi sortir
# key - function
# fungsi rot tidak peka pada huruf besar atau kecil
# sortir descending
def myfungsi(lol):
    return abs(lol - 50)

listangka1 = [3, 35, 32, 53 ,53, 2, 4]
listangka1.sort(key = myfungsi)
print(listangka)

# cara untuk membalikan list 
# reverse

my_new_list.reverse()
print(my_new_list)

# copy list
listbaru2 = [1, 4, 8, "satria", 7]
print(listbaru2)
listlagi = listbaru2.copy()
print(listlagi)

# cara lain untuk copy list
listlagi2 = list(listbaru2)
print(listlagi2)

# menggabungkan 2 list menjadi 1
list1 = [1, 4,2 ,53,5 ,22]
list2 = ["teknik", "informatika", "hallo"]
list3 = list1 + list2
print(list3)

# dengan fungsi append
for baru in list2:
    list1.append(baru)
    
print(list1)

# dengan fungsi extend
list1.extend(list2)
print(list1)
