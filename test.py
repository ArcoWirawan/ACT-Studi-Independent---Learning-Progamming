# from datetime import datetime as dt

# today = dt.now()

# print(today)

# tanggal = int(input("Tanggal = "))
# bulan = int(input("Bulan (1 - 12) = "))
# tahun = int(input("Tahun = "))

# birthday_date = dt(tahun, bulan, tanggal)

# birthday_format = birthday_date.strftime("%d %B %Y")
# print(birthday_format)

# dataSiswa = {
#     "siswa1": {
#         'nama':'tiana ramadhani',
#         'kelas':'10 TKJ'  
#     },
#     "siswa2": {
#         'nama':'Qience Mauline',
#         'kelas':'11 TKJ'
#     }
# }


# listMenu = """
# LIST MENU MAKANAN

# 1. Ayam Goreng = 15.0000
# 1
# """
# print(listMenu)

# inputPilihanMakanan = int(input("Pilih Makanan [1/2/3]"))
# quantit

# # if inputPilihanMakanan == 1:
# #     harga = 15.000
# # elif inputPilihanMakanan == 2:
    
# print('\n')
    
# data = {
#     'name':'arwanzxp'
# }

# print(dir(data))



name = "aarwannzxp"
division = "Network Engineer"

## ubah variabel global di dalam function
def MySelf(new_name,  new_division):
    # 1. global = memberikan izin untuk mengubah variabel di luar fungsi
    global name
    global division
    
    # 2. ubah isi variabel dengan isi dari parameter
    name = new_name
    division = new_division
    
    print(f"{name} - {division}")
    