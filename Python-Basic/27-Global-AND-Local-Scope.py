### merupakan cara bagaimana variabel dapat diakses dalam function

# variabel global scope
var1 = "aarwannzxp"



def YearBirth():
    print(f"Dia lahir bulan {var1}")
    
# var access to global

for x in range(0, 10):
    print(f"Loop {x} - {var1}")
    
    

# variabel local scope
# variabel yang umum di dalam loop

def HiToAll():
    qoute = "Hi, I hope a like day" # variabel local 
    return



## Contoh 1: penggunaan akses variabel
def Welcome():
    print(f"Selamat datang, di {name_toko} selamat berbelanja")

name_toko = "Toko Merah" # variabel global (diluar fungsi)
# dapat digunakan sebelum fungsi itu dipanggil
print(Welcome())


## Contoh 2 : merubah global var
# nilai var asli
Grade = 60
name = "M. Dika"

# fungsi untuk mengganti value var
def GradeModify(new_grade, new_name):
    global name # untuk mengakses var global
    global Grade
    Grade = new_grade # variabel global akan diganti valuenya oleh argument function 
    name = new_name
    
print(GradeModify())
GradeModify(80, "aarwannzxp")
print(Grade<())
    
# ubah angka using OOP
# Contoh 3 : 
number = 0


# for x in range(0, 5:
#     number += 1
#     dummy_number = 0
    
    

if True:
    number = 5
    dummy_num = 10


    
print(number)
print(dummy_num)
    
    





