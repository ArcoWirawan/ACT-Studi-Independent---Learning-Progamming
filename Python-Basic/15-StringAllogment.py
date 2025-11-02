# String width and Alignment 12/10/25

# string multiline

angka1 = 10
angka2 = 30

var1 = f"Hasil dari 10 ^ 2 = {angka1**2}"
var2 = f"Hasil dari {angka1} + {angka2} = {angka1 ** angka2:,}"

print(var1)
print(var2)


# string multiline (triple qouted)
try:
    inputNama = str(input("Nama = "))
    inputKelas = int(input("Kelas = "))

    student_01 = f"""
Nama    : {inputNama}
Kelas   : {inputKelas}

"""

    print(student_01)
except KeyboardInterrupt:
    print(f"\n{5*"="}exit{5*"="}")


####