## file ini untuk menjalankan kode yang ada di directory Rumus/file.py

# cara pemanggilan librarynya #

# # . = perpindahan directory (seperti /)
# import Rumus.math

# dengan fungsi tertentu
from Rumus import math

from Rumus import physic as fisika


while True:
    number_input = int(input("Masukan angka = "))
    operation = input("Masukan operasi [+ - x :] = ")
    
    operasi = 0
    match operation:
        case '+':
            operasi = math.Tambah(number_input)
        case '-':
           operasi =  math.Kurang(number_input)
        case 'x':
            operasi = math.Kali(number_input)
        case ':':
           operasi =  math.Bagi(number_input)
           
    
    print(f"Hasil = {operasi} ")
    if KeyboardInterrupt:
        break



# print(nambah)
print(fisika.gaya(10, 2))


# print(math(10, 5))