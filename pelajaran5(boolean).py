# python boolean
# pada pelajaran tentang boolean hanya terdapat 2 value untuk output
# True atau False

# contoh
from tkinter import FALSE


print(5 == 5) # True 
print(7 > 4) # True
print(5 < 3) # False

# boolean dengan if

a = 100
b = 222

if a > b:
    print("nilai pada variabel a = ",a ,"lebih besar dari nilai b = ",b)
else:
    print("nilai b = ",b, "lebih besar dari a")

# mengevaluasi nilai pada variabel
print(bool("helo"))
print(bool(2))

# kebanyakan value merupakan True
bool(2)
bool("sign")
bool(["1", 2, "satria"])

# value yang mengandung nilai False

bool(False)
bool(None)
bool(0)
bool([])
bool({})
bool(())

# cara untuk mengembalikan nilai 0 atau False
class myclass():
    def __len__(self):
        return 0 
myobject = myclass()
print(bool(myobject))

# cara membuat fungsi yang mengembalikan nilai boolean 
def fungsi():
    return True

print(fungsi())

# cara mengeksekusi kode berdasarkan jawaban boolean dari suatu fungsi
def myFungsi():
    return False
if myFungsi():
    print("iya")
else:
    print("tidak")
    
# cara menentukan apakah suatu obj memiliki tipe dara tertentu
# memakai fungsi isinstance()

sa = 100
print(isinstance(sa, int)) # jika benar True
                            # jika salah False