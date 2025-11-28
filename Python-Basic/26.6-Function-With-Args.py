"""
args = berguna untuk menampung banyak input, yang kemudian disimpan dalam bentuk tuple

ketimbang harus membuat banyak parameter (dalam kondisi tertentu!!)
    
1. *args (Non-Keyword Arguments)

    Wujud Asli: Tuple (item1, item2, item3)

    Analogi: Antrean Kasir. Si kasir (fungsi) nggak peduli nama orangnya siapa, dia cuma peduli urutannya. "Orang pertama", "Orang kedua", dst.
    
"""

def Fungsi(mahasiswa): # parameter data type = list
    mahasiswa_data = mahasiswa.copy() # copy data dari param ke var ini
    # ambil data secara berurutan (anggap input yang berurut)
    nama = mahasiswa_data[0] 
    prodi = mahasiswa_data[1]
    divisi = mahasiswa_data[2]
    
    print(f"Nama {nama}, prodi {prodi}, divisi {divisi}")
    
    
Fungsi(["arco","informatika","Network Engineer"])


"""
=== MENGGUNAKAN fungsi Args ===
Hanya perlu (*) dalam param function, yang dimana
memanggil semua parameter yang ingin masuk 
(bebas mau masuk berapa param juga)
"""

def Fungsi(*mhs_input):
    name = mhs_input[0]
    prodi = mhs_input[1]
    division = mhs_input[2]
    
    print(f"Nama {name}, prodi {prodi}, divisi {division}")
    
nama = str(input("Nama : "))
prodi = str(input("Prodi : "))
divisi = str(input("Divisi : "))
# class_kode = input("Kode kelas : ")
Fungsi(nama, prodi, divisi)

    
### Bisa digunakan untuk kalkulator ###

