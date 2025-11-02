## Loop dalam s

# 1.1 create triangle siku
# used for loop function

# segitiga siku
sisi = 10 # 1. seberapa banyak sisi yang mau digunakan

number = 1 # 2. penghitung bintang dari bari pertama
for x in range(sisi): # 3. lakukan perulangan sesuai sebanyak var sisi (10x)
    print("*"*number)
    number += 1

 
print("\n")

# 2.1 used while

number2 = 1
while True:
    print("*"*number2)
    number2 += 1
    if number2 >= 20: # im did 20 loops (SAYA MELAKUKAN 20X LOOP)
        break

print('\n')

# masih di materi yang sama
number3 = 1
# while True:
#     print("*"*number3)
#     number3 += 1

#     if number3 > sisi: # 
#         break 



print('\n')
print('\n')



## 2.2 Print pada kondisi tertentu

number4 = 1 
while True:
    if number4 == 20: break # jika loop sampe ke angka 20: stop paksa
    if number4 % 2: # jika angka loop genap: lakukan print
            print("*"*number4)
            number4 += 1
    else: # jika ganti : skip
        number4 += 1
        continue

    # bil genap 1 - 20 = 10
    # yang bakal ke print hanya 20 baris


print('\n')
print('='*5,"SOAL","="*5)
print("\n")

count = 2 # variabel objek loop (evert plus or min tergantung kebutuhan)
space = 5

while True:
     if (count%2): # 1 % 2 
          print(" "*space,"*"*count, f" Angka = {count} ")
          count += 1
     else:
          count += 1
          continue
     if count > 10:
          break
     






    
