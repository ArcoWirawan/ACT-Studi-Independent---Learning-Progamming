# gunakan fungsi type('data') untuk mengetahui data type pada var

# 1. Contoh langsung ke data float aja
print("+++ Float +++")
data1 = 10.90 

print(f"Data yang digunakan adalah {type(data1)}") # dan output dari type => <class 'float'>

# Convert Data type

conv_int_data1 = int(data1)
conv_bool_data1 = bool(data1)


print(conv_int_data1) # dibulatkan ke bawah
print(conv_bool_data1) # Selagi var ada isi data, status TRUE

# 2. convert data float
print("+++ Integer +++")

data_int = 10
conv_int_flo= float(data_int) # convert str, float sama aja

print(data_int, "Type = ", type(conv_int_flo)) # status float


# coba nanti var data_int ubah ke 0 dan lihat status dari bool
conv_int_bool = bool(data_int)

print(data_int, "Status = ", conv_int_bool)

# Cara Membuat status False
# ganti angka ke 0 (int dan float berlaku)
# Str kosongin
# Hasil => 0 Status =  False


# 3. Convert data Boolean
print("+++ Boolean +++")

data_bool = True

# akan memunculkan angka 1
print(f"Convert ke Int = {int(data_bool)}")
print(f"Convert ke Float = {float(data_bool)}")

# hanya berubah statusnya ke string
print(f"Convert Ke String = {str(data_bool)}")


