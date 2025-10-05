## Bitwise = Masing masing bit

# & | (XOR = ^) (~)

# int 2 -> 00000010 # membedakan angka berdasarkan binarynya

# int 10 = 00001010


bit1 = 10
bit2 = 30

bit_o1 = bit1 | bit2


print(f"Binary dari {bit1} = {format(bit1, '08b')}") # format(var, 'data')
print(f"Binary dari {bit2} = {format(bit2, '08b')}") 

print("===HASIL PERBANDINGAN BITWISE OR===")
# 1. bandingkan bit angka 1 dan 2 lalu turunkan
# 2. Dan bandingkan bit dengan operasi OR
# 3. bayangkan 8 baris digit seperti matematika susun
print(f"nilai {bit_o1} = {format(bit_o1, '08b')}") 
print(bit_o1)

print("\n=== Bitwise AND (&)")
bit_3 = 100
bit_4 = 50

bit_o2 = bit_3 & bit_4 
print("Hasil angka ", bit_3, " = ",format(bit_3,'08b'))
print("Hasil angka ", bit_4, " = ",format(bit_4,'08b'))

print("Hasil = ", format(bit_o2, '08b'))


### Operasi XOR (^)

bit_5 = 10
bit_6 = 11

number1 = 0b10010111
number2 = 0b10101100

print(format(number2,'08b'))
print(format(number1,'08b'))


print(f"angka {number2} dan {number1} = {format(number2^number1,'08b')}")


# shift binary ke kanan #
bit_7 = 99
shift7 = bit_7 >> 1

# Output ini akan mencetak nilai desimal dan biner dari 99
print(f"{bit_7} = {format(bit_7,'08b')}")
# Output: 99 = 01100011

# Output ini akan mencetak nilai desimal dan biner dari 49
print(f"Geser Biner {bit_7} = {format(shift7,'08b')}")
# Output: Geser Biner 99 = 00110001 






