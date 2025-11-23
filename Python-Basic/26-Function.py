import datetime
## fungsi biasa dipanggil :
## - method (dosen)
## - function

# fungsi = untuk mengelompokkan kode dan menghindari banyaknya kode yang tertulis ulang

# fungsi ini akan menjalankan input nama 
def Sapa():
    nama = str(input("Welcome, What's your name = "))
    print(f"Welcome {nama}")
    print(f"sekarang pukul {datetime.datetime.today()} ")
    

# jalankan fungsi seperti berikut -> NameFunction()
while True:
    Sapa() # menjalankan fungsi
    
    is_end = str(input("Lanjut?? [y/n]"))
    
    if is_end.lower() == "y":
        print()
    elif is_end.lower() == "n":
        print("\nExit Program")
        break
    else:
        print("input lu salah!!")
        break
        

#  