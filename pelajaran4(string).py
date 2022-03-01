# membuat tulisan dalam bentuk string
# dengan fungsi print

print('hello World')

# menggunakan variabel untuk mengumpulkan sebuah kata

a = "satria"
print(a)

# membuat multiline string

b = """sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
print(b)
# string merupakan array
# cara mengambil salah satu index dalam sebuah string

c = "satria dhapa"
print(a[4])


# looping dengan string
# cara memecah setiap huruf dalam string dengan for loop
for x in "satria":
    print(x)
    
# cara menghitung panjang string

d = "Teknik Informatika sarjana komunikasi"
print(len(d))

# cara mengecek ada atau tidak sebuah kata dalam sebuah string

text = "semua yang ada di mobil gratis"
print("gratis" in text) # akan mengeluarkan output booleans

if "gratis" in text:
    print("ada")
else:
    print("tidak ada")
    
# cara mengiris / slicing string 
# dari index ke -.. sampai akhir

text1 = " aku mencintai mu sampai mati"
print(text1[4:])

# dari awal sampai index ke - ...
print(text1[:4])

# memulai pengirisan dengan angka negatif atau dari depan ke belakang
print(text1[-5:-1])

# memodifikasi string
# cara untuk mengganti ke huruf besar

print(text.upper())

# cara untuk mengganti ke huruf kecil

print(text1.lower())

# cara unutk menghapus spasi pada string
print(text1.strip())

# cara mengganti salah satu huruf dalam string
print(text1.replace("a", "i"))

# cara memisahkan string
print(text1.split(" "))

# penggabungan string
# cara menggabungkan string

kata1 = "satria"
kata2 = "dhapa"
full = kata1 + " " + kata2
print("nama saya", full)

# format string
# cara salah dalam menggunakan format string
# umur = 36
# textt = "umur saya " + umur
# print(textt) # akan terjadi typeError

# cara yang benar dalam memakai format dalam string 

umur = 36
textt = "umur saya {}"
print(textt.format(umur))

# contoh lain untuk pemakaian format dalam string
# 1
kualitas = 1
item = 333
harga = 34.22
order = "aku ingin {} salah satu dari {} dengan harga {}"
print(order.format(kualitas,item,harga))

# 2 dapat disesuaikan sesuai index yang ingin kita inginkan
order1 = "aku ingin {1} salah satu dari {0} dengan harga {2}"
print(order1.format(kualitas,item,harga))

# cara keluar dari jebakan kesalahan string
# texxt = "kita biasa di panggil "viking" " # terjadi kesalahan
# tambahkan  \"
texxt1 = "kita biasa di panggil \"viking\" dari utara"
print(texxt1)

# macam - macam karakter yang dapat digunakan untuk keluar dari jebakan error di string
# \' single quotes
# \\ backslash
# \n new line
# \r carriege return 
# \t tab
# \b backspace
# \f form feed 
# \ooo octal value
# \xhh hex value

# module string python
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	    Returns a centered string
# count()	    Returns the number of times a specified value occurs in a string
# encode()	    Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()		Searches the string for a specified value and returns the position of where it was found
# format()	    Formats specified values in a string
# format_map()	Formats specified values in a string
# index()		Searches the string for a specified value and returns the position of where it was found
# isalnum() 	Returns True if all characters in the string are alphanumeric
# isalpha()	    Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	    Returns True if all characters in the string are digits
# isidentifier()Returns True if the string is an identifier
# islower()	    Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace() 	Returns True if all characters in the string are whitespaces
# istitle()	    Returns True if the string follows the rules of a title
# isupper()	    Returns True if all characters in the string are upper case
# join()		Joins the elements of an iterable to the end of the string
# ljust()		Returns a left justified version of the string
# lower()		Converts a string into lower case
# lstrip()	    Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	    Returns a string where a specified value is replaced with a specified value
# rfind()		Searches the string for a specified value and returns the last position of where it was found
# rindex()	    Searches the string for a specified value and returns the last position of where it was found
# rjust()		Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	    Splits the string at the specified separator, and returns a list
# rstrip()	    Returns a right trim version of the string
# split()		Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()		Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()		Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()		Converts a string into upper case
# zfill()		Fills the string with a specified number of 0 values at the beginning