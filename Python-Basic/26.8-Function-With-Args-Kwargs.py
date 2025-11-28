## Penggabungan kedua fungsi 
# Args dan Kwargs
# ##

## studi case
import os

os.system('clear')

# args harus menyimpan data int, selain dari int error
# tambahkan angka 1 + 2 + 3 + 4 dengan opsi +
# number -> *args
# operasi + - * / dsb -> **kwargs
def Mtk(*args:int, **kwargs):
    output = 0
    if kwargs['option'] == "+":
        for number in args:
            output += number
    elif kwargs['option'] == "-":
        for number in args:
            output -= number      
    else:
        print("Operation not found")
        
    # jangan sampe sejajar sama if else!!    
    return output
    

# data yang diinputkan
result1 = Mtk(1,2,3,4,option="+")
print(f"Hasil jumlah = {result1}")


