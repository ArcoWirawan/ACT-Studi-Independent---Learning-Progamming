## Looping Dictionary

community_member = {
    "wan":"Ridwan M",
    "dib":"M. adib",
    "ben":"benni"
}

count_member = range(len(community_member)) # data member = 3

# disini gua pake zip function dengan 2 var buat loop

for number,member in zip(count_member, community_member):
    print(f"{number+1}.{member}") 
    # 1. wan
    # 2. dib
    # 3. ben
    
    
print('\n')


"""
## Fungsi baru ini
1. keys() = mengambil data key saja
2. values() = mengambil data value saja
3. items() = mengambil data keduanya yang disimpan di tuple

"""
## 1. use keys function
keys = community_member.keys()
print(keys)

# 1. dalam in dia memanggil fungsi .keys() : buat ambil keysnya aja
for names in community_member.keys():
    # 2. dilakukan print pada variabel utama, dengan mengambil data pada var loop yang menggunakan fungsi keys (.get() function)
    # 3. pada fungsi get, panggil var loop yang menyimpan semua keys
    print(community_member.get(names))


print('\n')
# 2. values function
# untuk mengambil value di dict secara langsung

#  demo values function
values = community_member.values()
print(values)

# example 
for memberName, num in zip(community_member.values(), count_member):
    print(f"{num+1}.{memberName}")
  
print('\n')  
# 3. items function
item = community_member.items()

print(item)

for items in community_member.items():
    print(items) # menyimpan 2 output yang dapat dipisahkan oleh var loop

for nickname,realname in community_member.items():
    # output : key = value
    print(f"{nickname} = {realname}") 