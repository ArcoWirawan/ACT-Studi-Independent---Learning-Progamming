### Perulangan 

### Kode akan berputar selagi kondisi true
### 

# 1. Menggunakan for
# for (var sementara) in aksi}:
#       aksi

# 1.1 default range
x = 0 # First number
for x in range(5): # akan mengulang angka dari 0 ke 4 (4 = 5-1)
    print(x) # 0 - 4 (angka awal : var; angka akhir : range - 1)

print("\n")
# 1.2 list range
list1 = [0,1,2,3]
for y in list1:
    print(y) # data berurut sesuai index yang ada, bukan angka data dalam list!!

print("\n")
# 1,3 range function on the var
range_var = range(5) # 0 -4 : karena angka decimal
for z in range_var: # hanya panggil var, tidak perlu menggunakan fungsi range lagi
    print(f"Angka -> {z}") # Angka -> 0 s/d 4

# 1.4
menu_makanan = ["Soto Lamongan", "Mie Ayam Pasundan", "Guded"]
listNum = [1,2]
for a in listNum:
    for b in menu_makanan:

        print(f"{a}.{b}")
