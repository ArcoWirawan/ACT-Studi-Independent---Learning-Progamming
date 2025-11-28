## fungsi seperti biasa paham lah ya


## sekarang menggunakan lambda



# format -> lambda (arguments) : (expression)

# sama seperti halnya function, hanya saja function 
# dipresentasikan oleh kata lambda
kuadrat = lambda number : number**2
print(f"Hasil lambda kuadrat = {kuadrat(10)}")



addtion = lambda a : a + a
print(addtion(10))


# sortir untuk list biasa
list_data = ["arwanzxp", "hinrenz", "venzz"]

list_data.sort()
print(f"Sorted list = {list_data}")

# fungsi untuk key dalam fungsi sort
# menghitung panjang nama anak 
def panjang_nama(nama):
    return len(nama)

# menempatkan fungsi di dalam fungsi sort
# fungsi sort bekerja diawal menerima data, lalu data diolah oleh fungsi key
list_data.sort(key=panjang_nama)
print(f"Sorted List by length = {list_data}")



### filter number
number_data = [1,2,3,4,5,6,10,12,15,13,17]

def kurang_dari_10(number):
    return number < 10

# dalam list ada fungsi filter(fungsi filter, variabel yang ingin difilter)
new_number_data = list(filter(kurang_dari_10,number_data))

print(f"Data kurang dari 10 = {number_data}")

new_number_data2 = list(filter(lambda num : num < 15, number_data))
print(new_number_data2)


## Genap Case

data_genap = list(filter(lambda x: x % 2 == 0, number_data))
print(f"Angka ganjil = {data_genap}")

## Ganjil case

data_ganjil = list(filter(lambda y:y % 2 != 0, number_data))
print(f"Angka ganjil = {data_ganjil}")


## anonymous function


# program awal
def Eksponen(number, b):
    result = number ** b
    return result

eks_result =  Eksponen(10, 2)
print(f"Hasil dari 10 pangkat 2 = {Eksponen(10, 2)} ")

# dengan currying

def Pangkat(n):
    return lambda num: num**n 

# var baru
Pangkat3 = Pangkat(3)
print(f"Pangkat 3 = {Pangkat3(3)}") # panggil var yang menyimpan function menjadi list 3 x 3



