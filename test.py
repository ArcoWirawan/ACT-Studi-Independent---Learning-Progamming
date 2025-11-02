from datetime import datetime as dt

today = dt.now()

print(today)

tanggal = int(input("Tanggal = "))
bulan = int(input("Bulan (1 - 12) = "))
tahun = int(input("Tahun = "))

birthday_date = dt(tahun, bulan, tanggal)

birthday_format = birthday_date.strftime("%d %B %Y")
print(birthday_format)