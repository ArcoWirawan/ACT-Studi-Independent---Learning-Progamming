### STRING INTRODUCTION
### Kegunaan : untuk menyimpan data karakter (angka, simbol, dll)


"""
    Jenis String
    1. single qouted (petik 1)
    2. double qouted (petik 2)
"""

print("Halo, Aku ArwanzXP. Terhitung belajar progamming 30 September 2025") # Double Qouted
print('bismillah jago jaringan jago ngoding wkwk')

### Single Qouted Problem
# print('Aku harus ngaji di hari Jum'at') ## dicoba aja pasti merah

# itu karena adanya kutib ganda diakhir, dianggap fungsi string

## 1. Mitigasi : gunakan (\') 
# ini adalah karakter regex (regular expansion) untuk menseleksi tanda baca khusus!! (konteks regex)
# bisa digunakan untuk menambah efektivitas kode


print("\n1. Regex = petik 1 ditengah(')")
# Ketika di print, akan normal seperti penulisan karakter biasanya
print('Aku ngaji di masjid unpam hari jum\'at') 


# 2. Regex = Tab
print("\n2. Regex = Tab")
print("Tinggal di Bogor \t Ciseeng, Bogor.") # Tinggal di Bogor         Ciseeng, Bogor.

# 3. Regex = New Line
print("\n3. Regex = New Line")
print("Aku suka kopi Amerikano\nKalo gapunya duit kopi liong") # LF -> line feed -> unix, mac, linux
print("\nAku suka kopi Amerikano \rTapi kalo akhir bulan kopi liong") #CR -> Carriage return -> pemograman dan OS lama (commodore, accorn)
print("Aku suka kopi Amerikano \r\nBut, kalo duit abis ya kopi liong") # CRLF -> gabungan keduanya -> windows

# 4. Regex = Backslash
print("\n4. Regex = Backslash")
# apabila kalian melakukan backsplash secara solo
# maka akan dianggap regex char
# cara = regex backslash (\\)
print("C:\\ArwanzXP\\Document") 


# 5. Regex = backspace
print("\n5. Regex = backspace")

# menghilangkan spasi / menghapus 1 karakter
print("Arwanz \bXploit") # jadi nyatu nantinya


# 6. String Literal (raw)

# sampel : penulisan kode untuk dir yang salah berikut:
# print("C:\network")

# gunakan raw string (r)
print(r'C:\users\arwanzxp') #karakter regex akan dijadikan string semua 



# 7. multiline literal string

myName = "aarwannzxp"
myDivision = "Network Engineer"
print(f""" 
nama : {myName}      
divisi : {myDivision}
""")

# multiline dengan regex
# r (raw); f(f-string)
print(rf""" 
user : {myName}
yourDir : C:\users\{myName}

""")




