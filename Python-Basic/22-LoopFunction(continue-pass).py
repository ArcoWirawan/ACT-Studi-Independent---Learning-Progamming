### fungsi dalam loop
### continue, pass, break

# continue  = skip pada kondisi tertentu dalam perulangan
# pass      = berfungsi sebagai dummy, tidak akan di exec (tidak dipakai)
# break     = berhentikan paksa loop


## Source Code 1

number = 5

# while number > 0:
#     number -= 1
#     print(number)
#     if number == 2:
#       break

## continue


while number > 0:
    number -= 1
    print(f" {number}")
    if number == 2:
        print("Diam diam saja") # akan muncul di angka 2
        continue # cut fungsi setelahnya 
                 # jadi tidak memunculkan "Okey"

    print("Okey")


## latihan

print("\n")

number = 20
while number > 0:
    number -= 1 # print loop    
    print(f"Angka ke - {number}") # 2. baru print ini (setiap kali)
    if number == 11 and number == 7:
        print("Jangan lupa angka ini")
        continue

    print("OKE!!")


print('\n')

number = 10
while number > 0:
    number -= 1
    print(f"{number}]Mundur")
    if number == 3:
        break
    print("Haha")


