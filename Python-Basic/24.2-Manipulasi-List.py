## 


# index 0(-3) 1(-2) -2(1)
data  = ['rudi', 'hamid', 'budi']

data_0 = data[0]
print(f"Orang pertama dalam list adalah {data_0}")

end_data = data[-2]
print(f"Data terakhir adalah {end_data}")

# get info about count data on list
print(f"Data pada list ada {len(data)}")




## List manipulation ##

# add item on list 
data.insert(1, "arwanz") # add to array 1, value = arwanz
print(data)

data.append("Galih") # add data on new array
print(data)

# new list data
new_data = ["Nawa","Bagus"] 
data.extend(new_data)
print(data) # ['rudi', 'arwanz', 'hamid', 'budi', 'Galih', 'Nawa', 'Bagus']

# change data
# we change data 2 become pali
data[1] = "pali"
print(f"perubahan data = \n{data}")

## remove data
data.remove("Galih") # harus sesuai dengan input namanya
print(data) 

data.pop() # delete data on end array number
print(data) # Bagus terhapus

data.pop(0) # 
print(data) # Rudi terhapus