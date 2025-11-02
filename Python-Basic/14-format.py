## FORMAT FUNGSI
print("## FORMAT FUNGSI\n")

name = "Arco Wirawan"
print(name)

# 1. used format with (f"")
sayMe = f"Hello my name is {name}\n"

# 2. used (:) for modified string

# 2.1 number dengan orde bil yang banyak

# urutan =  
# sebelum koma
# sesudah kome
# format bilangan : d : decimal; f: float;

total = 2000
print(f"total pengeluaran = {total:,}")

# 2.2 Decimal number
number = 15
print(f"Angka = {number:d}")

# 2.3 number format (seperti membatasi angka)
bil_float =  10.429123123
print(f"Angka float pertama = {bil_float}")
print(f"Angka float = {bil_float:5.1f}")

# 2.4 format  leading zero
bilangan = 2011.92830
print(f"Angka asli = {bilangan}")


### NOTED GUYS!! :
# 5 = dihitung dari digit biner 0, 5 
# angka biner 5 tepat pada angka 10

# 3f = akan melakukan 

print(f"Angka format = {bilangan:1.1f}") # Angka format = 2011.9

#:.3f	Bulatkan menjadi 3 desimal,	12.346	Hanya presisi
#:10.3f	Bulatkan jadi 12.346 (6 char), siapkan lahan 10 char	12.346	Ditambah 4 spasi di depan
#:2.3f	Bulatkan jadi 12.346 (6 char), siapkan lahan 2 char	12.346	Lebar tidak berefek karena angka lebih panjang


# show arimath operator + and -
minus_number = -10
plus_number = 70

print(f"Format dong = {minus_number}")
print(f"Format angka positif ={plus_number:+}") 



# math operation with format function
print(f"Sisi Persegi panjang = {20 * 13}")


# format variant number
print(f"Angka biner = {bin(10)}") # conver angka 10 ke binarh
print(f"angka oktal = {oct(20)}")
print(f"Angka hexadevimal = ")


