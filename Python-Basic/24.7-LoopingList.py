## Looping dari list

# used for loop
print("used for loop")
number_group = [4,5,6,7,8]

for number in number_group:
    print(f"Angka = {number}")


member = ["andi", "rahmat", "udin"]

for mem in member:
    print(f"name = {mem}")


# for loop and range
print("\nWhile loop")
number = [10, 5, 20, 30]

panjang = len(number)
i = 0
##
for i in range(panjang):
    print(f"angka = {number[i]}")

