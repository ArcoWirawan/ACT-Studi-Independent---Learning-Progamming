###  1. Isikan datanya dulu

# anggap ini sebagai column and  row
data_1 = [1, 2] # row 1, column 2
data_2 = [3, 4] # row 2 , column sama
data_3 = [5, 6] # row 3

packed_data = [data_1, data_2, data_3, 8]
packed_data_cp = packed_data.copy()
print(packed_data) # kumpulan data

## 2.  get data on packed_data

get_data = packed_data[0]
print(get_data) # data 1 get

## 3. how get single data on packed data
# bagaimana caranya mendapatkan salah satu data dari packed data


# a. pilih mau ke list mana
# b. 
get_data = packed_data[0][0] # [column][row] 
# seperti halnya di ms.excel
get_data_cp = packed_data_cp[0][0]
print(get_data)

## 3. all address (hex)
print("\nTerlihat sama ya")
print(f"Real Address = {hex(id(packed_data))}") 
print(f"copy addr = {hex(id(packed_data_cp))}")

print('\n')
## get data adddress (num 3)

print("Coba lihat address saat data diambil")
print(f"Address asli = {hex(id(get_data))}")
print(f"Address copy = {hex(id(get_data_cp))}")

## 4 . Change real data
packed_data[1][1] = 10
packed_data[3] = 2

print("\nUbah angka 1 menjadi 10 di data asli (harusnya gak berubah yg di copy)")
print(packed_data)
print(packed_data_cp)

## 5. karena semua angka di list yang sudah dicopy berubah juga
# maka kita dapat menggunakan library (deepcopy)

## softcopy library

from copy import deepcopy

packed_data_before_deepcopy = [data_1, data_2, data_3, 2] # perubahan ke angka 10 tetap ada
packed_data_deepcopy = deepcopy(packed_data_before_deepcopy)

print(f"data = {packed_data_before_deepcopy}")
print(f"data copy = {packed_data_deepcopy}")


## cek address hex
print("Cek address nya lagi")
print(f"data asli = {hex(id(packed_data[0][1]))}")
print(f"real add = {hex(id(packed_data_before_deepcopy[0][1]))} ")
print(f"copy add = {hex(id(packed_data_deepcopy[0][1]))}")


# update data before deepcopy
packed_data_before_deepcopy[0][1] = 29
print(f"Data before deep = {packed_data_before_deepcopy}")  # list 1 
print(f"Data deepcopy = {packed_data_deepcopy}")