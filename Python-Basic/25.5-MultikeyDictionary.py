import datetime


mhs_1 = {
    'nama':'Arco Wirawan',
    'nim':298399,
    'sks-lulus':120,
    'beasiswa':False,
    'lahir':datetime.datetime(2007, 1, 25)
}
mhs_2 = {
    'nama':'Rudi Arwandara',
    'nim':298329,
    'sks-lulus':130,
    'beasiswa':True,
    'lahir':datetime.datetime(2007, 1, 15)
}
mhs_3 = {
    'nama':'Deva Virasco',
    'nim':298330,
    'sks-lulus':140,
    'beasiswa':False,
    'lahir':datetime.datetime(2007, 1, 1)
}

# kumpulan data setiap mahasiswa
mhs_data = {
    'MHS01':mhs_1,
    'MHS02':mhs_2,
    'MHS03':mhs_3
}

# buat header tabel sederhana
# :<(number) = mengatur range columnnya
print(f"{'Key':<10} {'nama':<20} {'SKS':<5} {'Beasiswa':<9} {'Lahir':<12}")
print("-"*50)

for mhs in mhs_data:
    KEY = mhs
    
    # 1. data diambil dari var mhs_data yang dimana masih var ini menyimpan var yang menyimpan data mahasiswa
    # 2. panggil identifier (mhs_data) lalu panggil key yang terdapat di dalam var (mhs_num)
    NAMA = mhs_data[KEY]['nama']    
    SKS = mhs_data[KEY]['sks-lulus']
    print(f"{KEY:<10} {NAMA:<20} {SKS:<5}")


