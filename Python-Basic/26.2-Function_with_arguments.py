## Informasi dapat diteruskan ke fungsi menggunakan arguments

# ditempatkan dalam tanda kurung setelah penamaan fungsi

# sebutan lain
# arguments => parameter
def ArwanzXP(nama_lengkap, divisi):
    print(f"Halo, gua {nama_lengkap}")
    print(f"Dan gua ada di divisi {divisi}")


ArwanzXP("Arco Wirawan", "Network Engineer")

print()


def Sambutan(tamu):
    """Fungsi Sambutan untuk menyambut tamu besar"""
    data_tamu = tamu.copy() # param tamu berdata list, disimpan dalam variabel dan dicopy datanya
    for tm in data_tamu: # lakukan perulangan untuk output
        print(f"Yang terhomat {tm}")

# data tamu        
tamu_besar = ["Bpk Suhendar, S.Kom", "Ibu Nurahma, S.Si"]

Sambutan(tamu_besar)

