### 1. menyambung string
# 1.1 Pakai Tambah

nama_depan = "Muhammad"
nama_tengah = "Ridwan"
nama_belakang = "Al-Khair"

print(nama_depan + nama_tengah + nama_belakang)

# 1.2 Menggunakan format string (fstring)
# setelah kurung, tambahkan huruf f sebelum masuk data string
# tulisan dalam kurung awal akan dianggap kode
print(f"Halo, my name is {nama_depan} {nama_belakang} {nama_belakang}") 


### 2. Menghitung panjang string
ThisStory = "Do what you like."
# make function : len(var) 
checkLength = len(ThisStory) # "17" string character 
print("Panjang dari qouted itu adalah", checkLength)
print("\n")

### 3. Operator untuk String
# mengecek keberadaaan komponen karakter dalam string

data01 = "Zahra" # Z kapital
searchChar = "z" 
# searchChar2 = "ruy"

print(searchChar in data01) # mencari z kecil = False
print("\n")

# menggunakan not in (negasi)
data01 = "Zahra Juli Azrina"
searchChar = "rara"

print(searchChar not in data01) # kata rara tidak ada di var data01 = True

### 4. Loop String
print("wk"*4) #kata 'wk' diulang 4x


### 5. Indexing 
# 5.1 index dimulai dari 0 (bil pecahan)

print("inisial nama", data01[0])

# index mundur (-1 = 1 karakter akhir)
print(data01[-2]) # cetak huruf n

# 5.2 Index start:stop
# start = dihitung dari index number
# stop = dihitung dari length number
print(f"Nama dia = {data01[0:5]}")


# 5.3 Index start:stop:step

dataangka = 2,4,6,8,10
print(dataangka[0:2:4])


