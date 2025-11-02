import datetime as dt # ambil library datetime dan beri alias "as"

# jika tidak mau ribet masalah datetime dipanggil 2x
# kita dapat memanggil function datetime dalam library datetimenya itu

# from datetime import datetime


# A. set manual datetime
# B. The strftime() method

HariIni = dt.date.today()
print("Hari ini = ", HariIni)


# A. set manual datetime

AcaraSeminar = dt.datetime(2025, 12, 18, 7)
print(f"Acara Seminar Teknik Informatika = {AcaraSeminar}")

# B. The strftime() method

TheFirstMyJob = dt.datetime(2025, 10, 6)

# B.1 Convert used the function
print(TheFirstMyJob.strftime("%B,%A %d"))

## B.2 Option
print(f"Hari pertama saya kerja = {TheFirstMyJob:%A}")


### PROJECT ####
# Create Input for data ultah
# Format >> 2011, July 29 

# tanggal = int(input("Tanggal = "))
# bulan = int(input("Bulan (1 - 12) = "))
# tahun = int(input("Tahun = "))

#birthday_date = dt.datetime(tahun, bulan, tanggal)

# karena datetime sudah tersedia pada birtday date
# disini hanya menambahkan strftime untuk mengubah penulisan tanggalnya
# FormatBirtday = birthday_date.strftime("%Y,%b %d") 
# print(FormatBirtday)


### REAL PROJECT ###

print(f"{"="*5}INPUT ULTAHMU{"="*5}") # header
days = int(input("Tanggal \t= "))
months = int(input("Bulan \t= "))
years = int(input("Tahun \t= "))

birthday = dt.datetime(years, months, days)
output_format_birthday = birthday.strftime("%B, %d %Y")


print("yeah ultahmu = ", output_format_birthday)

YourAgeNow = dt.datetime.today()
YourAge = YourAgeNow - birthday # umur = dalam bentuk hari

YearAge = YourAge.days // 365

sisaUmur = (YourAge.days % 365) // 30
print("Ummur gue = ",YearAge, " Tahun")
print(f"Ultah kedepannya tinggal {sisaUmur}")



