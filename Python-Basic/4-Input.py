# 1. menggunakan fungsi input()

input1 = input("Nama = ") # default data type = str

print("Type Data yang diinput = ", type(input1), " ", "Value = ", input1 )

# 2. Input sesuai data type
# data type - input fungsi - Text for input
# Berlaku untuk semua tipe data kecuali Bool
int_input = int(input("Masukan angka Biasa = ")) 
print(f"Angka yg dimasukkan = ")

# 3. Input Boolean
# data type req - convert int - text
bool_input = bool(int(input("Apakah kamu sudah S1 = ")))
print(f"S1 = {bool_input}")






