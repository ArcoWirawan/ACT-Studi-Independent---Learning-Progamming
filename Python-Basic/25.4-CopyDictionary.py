## Copy Dictionary

community_member = {
    "wan":"Ridwan M",
    "dib":"M. adib",
    "ben":"benni",
    "zan":"radzan maulana"
}

# 1. copy data
active_member = community_member.copy()
print(type(active_member)) # data type tetap dict


# change dict key = ben
active_member["ben"] = "Benni Zeque"
print(active_member)

print('\n')

# 2. pop (menghilangkan data dan memindahkan ke var lain)
# data ditransfer berdasarkan key

group1 = active_member.pop("ben")
print(f"Group 1 = {group1}")

# tambah data lagi via pop
group1 += "," + active_member.pop("zan")
print(f"Group 1 = {group1}")


# 3. popitem dictionary
group2 = active_member.popitem()
print(group2)



