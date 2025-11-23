"""Program data mahasiswa menggunakan dictionary"""
import datetime # WAKTU, HARI TANGGAL DSB
import os # AKSES OS SEPERTI HALNYA MENGGUNAKAN CMD
import string
import random



# Mahasiswa data template
mhs_template = {
    'nama':'nama',
    'nim':000000000000,
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

# menampung data mahasiswa
mahasiswa_data = {}

    ### os.system("command prompt") ###
while True:
    os.system("clear") # seperti menjalankan 

    ## header tengah 
    print(f"{'WELCOME':^20}") # geser tengah 
    print(f"{"DATA MAHASISWA":^20}")
    print("-"*20) # - s/d 20

    ## variabel untuk input data 
    mahasiswa = dict.fromkeys(mhs_template.keys())
    mahasiswa['nama'] = str(input("Nama mahasiswa = "))
    mahasiswa['nim'] = int(input("NIM"))
    mahasiswa['sks_lulus'] = int(input("SKS Lulur = "))
    DAY_BIRTH = int(input("Tanggal Lahir = "))
    MONTH_BIRTH = int(input("BULANG LAHIR = "))
    YEAR_BIRTH = int(input("TAHUN LAHIR = "))
    mahasiswa['lahir'] = datetime.datetime(YEAR_BIRTH,MONTH_BIRTH,DAY_BIRTH)
    
    ## komentar jangan lupa ya!!
    ## Buat string menjadi random
    ## dengan karakter string ascii dan huruf besar
    ## buat sebanyak 6 karakter (huruf dan angka random) = syntax for
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

    # masukan data ke variabel untuk menampung data mahasiswa
    mahasiswa_data.update({KEY:mahasiswa}) # dict mahasiswa_data dapat data dari var mahasiswa (var input)

    # tabel data mahasiswa
    print(f"\n{'KEY':<6} {'NAMA':<20} {'NIM':<12} {'SKS Lulus':<10} {'TTL':<15}")
    print(f"-"*90)

    # get and print mahasiswa data
    
    for mhs in mahasiswa_data:
        # key menyimpan input dari 
        KEY = mhs
        
        NAME = mahasiswa_data[KEY]['nama']
        NIM = mahasiswa_data[KEY]['nim']
        SKS = mahasiswa_data[KEY]['sks_lulus']
        TTL = mahasiswa_data[KEY]['lahir'].strftime("%x")
        
        print(f"{KEY:<6} {NAME:<20} {NIM:<12} {SKS:<10} {TTL:<15}")
        
        print()
        
    # end zona loop
    
    # perintah untuk konfirmasi lanjut tidaknya
    confirm_repeat = input("Lagi? [y/n]")
    if confirm_repeat == 'n':
        break
    
        
print("Thanks")

        
