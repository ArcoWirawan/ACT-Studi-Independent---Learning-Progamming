## assigment 
## penimpaan variabel dengan nilai lain dengan melakukan operasi math nya
## Berguna untuk mempermudah dalam melakukan aritmatika pada kode (gaperlu tampung nilai di var baru)
## += -= /= **= %=


# modulus = 
a = 10
a %= 7  

print(f"a = {a}")


#### bitwise assigment

b1 = True
print(format(b1,'08b'))
# Bitwise OR (biner dicocokan dengan OR)
b1 |= True

print(b1)
print(format(b1,'08b'))

b2 = 0b1010
print("Hasil binary b2 = ", b2)

b2 >>= 1 # setiap angka bit 1 digeser 1
print("Pergeseran = ", format(b2,'04b'))

# shift biner ke kanan 
b2 <<= 1
print(format(b2,'04b'))

