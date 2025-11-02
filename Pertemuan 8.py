print("==== Daftar Buku Toko | Rizki Febriansyah - 2510114006341 |")

priceBook = """
1. Pemrograman Python\t: Rp. 85.000
2. Logika Informatika\t: Rp. 65.000
3. Struktur Data\t: Rp. 90.000
"""

print(priceBook)
print("="*15)

select_book = int(input("\nPilih buku yang ingin dibeli [1/2/3]: "))

if select_book == 1:
    jumlah = int(input("Masukkan jumlah pesanan Pemrograman Python : "))
    jumlah *= 85000
    print(f"Jumlah harga yang harus dibayar : Rp.{jumlah}")
elif select_book == 2:
    jumlah = int(input("Masukkan jumlah pesanan Logika Informatika : "))
    jumlah *= 65000
    print(f"Jumlah harga yang harus dibayar : Rp.{jumlah}")
elif select_book == 3:
    jumlah = int(input("Masukkan jumlah pesanan Struktur Data : "))
    jumlah *= 90000
    print(f"Jumlah harga yang harus dibayar : Rp.{jumlah}")
else:
    print("Tidak ada pilihan angka!")
    print("exit")

thePayment = int(input("Masukkan jumlah uang : ").replace(".",""))
cashBack = thePayment - jumlah

print(f"Kembalian anda adalah = {cashBack}")