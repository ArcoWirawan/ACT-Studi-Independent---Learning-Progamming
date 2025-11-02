### COPY LIST DATA

rill_data = ["Andi", "Yudi", "Farhan", "Hamdan"]

print(rill_data)

copy_data = rill_data
print(copy_data)

print('\n')
## set data list[2]

print("ubah data list[2]")
rill_data[2] = "Arco"

print(rill_data)
print(copy_data)

copy_data2 = rill_data.copy() # duplicate use copy function
print("\n")
print(copy_data2)

# perhatikan pada bagian hex nya.
print(f"Memori variabel rill = {hex(id(rill_data))}")
print(f"Memori variabel copy = {hex(id(copy_data))}")
print(f"Memori variabel copy2 = {hex(id(copy_data2))}") # hanya sama di beberapa digit awal

# change data on list copy2
copy_data2[1] = "Yadi"
print(copy_data2)




