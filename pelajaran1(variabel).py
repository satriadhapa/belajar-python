# python variabel
# x = 5 # x adalah variabel
#         # 5 adalah isi variabel yang bertype int
# y = "satria" # y adalah variabel
#             # "satria" adalah isi variabel yang bertype string
# print(x , y) # print untuk mencetak 

# a = 4
# a = "dhapa"
# print(a) # output dhapa karena isi variabel seketika digantikan oleh nama variabel yang sama

# cara mencasting isi variabel
# a = str(3)
# b = int(3)
# c = float(3)

# print(a, b, c)

# cara mendapatkan type sebuah variabel

# d = 7
# e = "jhon"
# print(type(d))
# print(type(e))

# # isian variabel dapat memakai single quotes or double quotes
# x = "satria"
# y = 'satria' # dua dua nya dapat dianggap sah

# nama dari sebuah variabel sangatlah sensitif
# contoh
# A = "satria"
# a = "sekolah"
# # variabel diatas berbeda meskipun memakai nama ynag sama

# # contoh nama variabel yang dapat digunakan
# variabelku = "satria"
# variabel_ku = "satria"
# Variabelku = "satria"
# VariabelKu = "satria"
# VARIABELKU = "satria"

# contoh di atas merupakan varibel yang sah digunakan
# hindari penggunaan angka di awal variabelyang dapat
# menjadi kesalah syntax

# ada beberapa ciri khas pembuatan variabel
# camel case variabel
# namaVariabelku = "satriadhapa"
# # pascal case variabel
# NamaVariabelKu = "satria"
# # snake case variabel
# Nama_Variabel_Ku = "satria"

# membuat variabel dalam 1 line
# x, y, z = 1, 3 ,"satria"
# print(x)
# print(y)
# print(z)

# # membuat beberapa nama variabel dengan isian yang sama
# a = b = c = "satria"
# print(a)
# print(b)
# print(c)

# cara membuka isian sebuah list dengan variabelyang
# fruit = [1, "satria", 0.7]
# a, b , c = fruit
# print(a)
# print(b)
# print(c)

# # cara membuat global variabel
# x = "luar biasa"

# def fungsiku():
#     print("python sangatlah " + x)

# fungsiku()

# # membuat variabel dalam global variabel
# a = "amazing"
# def satria():
#     a = "luar biasa"
#     print("python sangatlah " + a)
# satria()

# print("python sangatlah " + a)

# # membuat kata kunci global variabel
# def satriaku():
#     global z
#     z = "luar biasa"
# satriaku()

# print("python memang " + z)

# membuat variabel dalam kata kunci global
y = "tidak biasa"
def satriaKu():
    global y
    y = "luar luar biasa"
satriaKu()

print("python memang " + y)