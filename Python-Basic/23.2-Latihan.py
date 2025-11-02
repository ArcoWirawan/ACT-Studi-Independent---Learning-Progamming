# create segitiga

# core variabel
side = 10

for x in range(side):
    print("*"*side)
    side -= 1


print("\n")


# --- while
# option 1 while
while side > 0:
    print("*"*side, "Angka ke ", side)
    side -= 1

# -- option 2
diloop = 10
while True:
    print("ArwanzXP")
    diloop += 1

    if diloop == 20: break # pembatas via if

###

diloop = 2

while True:
    print("Benar")
    diloop += 1

    if diloop % 2 != 0:
        print("Ganjil")
    else:
        print("Ganjil")

    if diloop == 20:
        break
print("==End ganjil genap status==")

print('\n')
print('\n')
print('\n')

# 1. SEGITIGA SAMA KAKI
count = 1 # variabel objek loop (evert plus or min tergantung kebutuhan)
space = 5

while True:
     if (count%2): # 1 % 2 
          print(" "*space,"*"*count)
          space -= 1
          count += 1
     else:
          count += 1
          
          continue
     if count > 10:
          break
     

## 2. berlian (belah ketupat)
count = 1
space = 1
