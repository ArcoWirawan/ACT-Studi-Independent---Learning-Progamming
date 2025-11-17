## Dictionary Operation
tongki_cafe = {
    # nama panggil, "nama panjang"
    "vanz":"Vandzra Mario",
    "wan":"arwanz",
    "wen":"Wendra Suwendar"
}

# data length dictionary
LENGTH = len(tongki_cafe)
print(f"Banyak temen di cafe {len(tongki_cafe)}")

# Check key exist or not on data
KEY = "vanz" # nama panggilan
# check keyvalid
print(f"Bocah ada yang dipanggil {KEY} = {KEY in tongki_cafe}")

print("\n")

##  value access (read) with get
print(tongki_cafe["wen"])
print(tongki_cafe.get("wan")) # mengecek dan output data dicti tanpa error jika salah
print('==')
print(tongki_cafe.get('arr', 'tidak tersedia')) ## karena key arr tidak ada, 
# status disebelahnya berjalan
print(tongki_cafe["wan"])


# data update (disini saya coba untuk mengganti data)
tongki_cafe["wan"] = "Arwanz kang multask"
tongki_cafe.update({"wen":"wendra S"}) # update nama asli
print(tongki_cafe)

# change data 
tongki_cafe["wan"] = "Arco Wirawan"
print(tongki_cafe["wan"])

# delete data
del tongki_cafe["wen"] 
print(tongki_cafe) # data wendi ilang

