##

number_data = [1,2,3,4,5,6,7,8,9,0,4,10,29,5,5]

print(f"Data = \n{number_data}\n")


# 1. count data
jumlah_data_4 = number_data.count(4)

print(f"Jumlah angka 4 = {jumlah_data_4}") 


## 2. look for the index of the data (mencari index dari sebuah data)

data = ["Ari", "Budi", "Naura", "Naomi"]

search = data.index("Ari") # index 0

print(f"Data ada di index {search}")

input1 = str(input("Input nama = "))
search = data.index(input1)

print(f"Data ada di index {search}")

## 3. sorting (urut)

number_data.sort()
print(number_data) #  Before : [1,2,3,4,5,6,7,8,9,0,4,10,29,5,5]

## 4. balik data (reverse)

number_data.reverse()
print(number_data) # [29, 10, 9, 8, 7, 6, 5, 5, 5, 4, 4, 3, 2, 1, 0]

