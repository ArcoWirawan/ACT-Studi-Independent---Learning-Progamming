"""Function with return"""

# template

# def name_func(argument):
#     badan fungsi
#     return output

def SisaBagi(number1, number2):
    sisa = number1 + number2
    
    # return = mengembalikan data ke kode pemanggil (buat diolah komputer) 
    # return TIDAK DIANJURKAN untuk output
    return sisa

    ## return tidak disarankan untuk output seperti ini
    # return number1, " + ", number2, " = ", sisa
    
    ## melainkan output tersebut masih bisa diproses
    ## jatuhnya ini dibungkus dalam satu tuple
    ### solusi : pisahkan operasi perhitungan dengan output teks
    
    # return f"Hasil tambah dari {number1} + {number2} = {sisa}"

Bagi1 = SisaBagi(10,3)
print(Bagi1)

Bagi1 += 100
print(f"Hasil setelah ditambah 100 = {Bagi1}")

"""Dummy Code
karena return hanya memproses data
"""
# Bagi2 = Bagi1 + 100
# print(Bagi2)


# function with many return
def Calculator(num1, num2):
    addtion = num1 + num2
    subtraction = num1 - num2
    mutliplication = num1 * num2
    division = num1 / num2
    
    return addtion, subtraction, mutliplication, division



z = Calculator(100,3)
print(z) # output : (103, 97, 300, 33.333333333333336)
         # data type : tuple

# gunakan konsep Tuple Unpacking
a,b,c,d = Calculator(50,7)

print(f"Hasil tambah = {a}")
print(f"Hasil kurang = {b}")
print(f"Hasil kali = {c}")
print(f"Hasil bagi = {d}")
    
    
print()
"""DEFAULT ARGUMENT"""

# berikan argument(parameter)
def katakan_pagi(nama="aarwannzxp"):
    print(f"Selamat Pagi, {nama}")
    
    
katakan_pagi()

# kita dapat mengubah isi argument

katakan_pagi(nama="kii")