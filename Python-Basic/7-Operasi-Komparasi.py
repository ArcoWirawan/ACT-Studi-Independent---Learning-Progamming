###

### >, <, <=, >=, ==, !=, is, is not

# setiap komparasi menghasilkan nilai boolean

# 1. > and < (angka harus lebih besar / kecil)
p1 = 4 > 5
print(f"4 > 5 =  {p1}")

var01 = 10
print(var01 < 20)

# menggunakan 
var02 = 10.000001
print(f"{var02} > 10 = {var02 > 10}")

# 2. <= and >= (data yang masih dianggap true)
p2 = 3 <= 3
print(p2) # TRUE


# 3. == and != (Data)
var03 = 100 
print(f"Result from {var03} == 100 = {var03 == 100}")

# Tidak sama dengan
print(f"var03 != 100 = {var03 != 101}") # jika nilai tidak sama = True


### is dan is not ###
# membandingkan nilai berdasarkan memorinya 0x123...
# komparasi object identity
# data akan disimpan pada memory yang sama

is_a = 10
is_b = 29

# Memori is_a
print(f"var is_a memory = {id(is_a)}") # id = untuk melihat  memori dari variabel
print(f"var is_a hexadecimal memory = {hex(id(is_a))} ") # 0xa3fb50


print(f"var is_b memory = {id(is_a)}")
print(f"var is_b hex memory = {hex(id(is_b))}")



print(f"Hasil Perbandingkan is = {is_a is 10}")


### is not ###

isNot1 = 10
isNot2 = "10"

print(f"Perbandingan data var 1 & 2 = {type(isNot1) is not type(isNot2)}") # secara tipe data sudah beda, makanya bener ya


print(isNot1 != isNot2)


 






