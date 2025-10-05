##### ------3---------10++++
## angka yang < 3 atau > 10

orLogic1 = int(input("Angka lebih dari 3 atau lebih dari 10 = "))

print(f"< 3 = {orLogic1 < 3}")
print(f"> 10 = {orLogic1 > 10}")

print(f"Hasilnya = {orLogic1 < 3 or orLogic1 > 10}")

## angka yang lebih dari 2 kurang dari 8 dan termasuk angka ganjil
andLogic1 = int(input("angka yang lebih dari 2 kurang dari 8 dan termasuk angka ganjil = "))

print(f"Hasil dari soal logic 2 = {andLogic1 > 2 and andLogic1 < 8 and andLogic1 % 2 != 0} ")


## Soal Tambahan

## 1. ----0++++5-----8++++11----
inputS1 = int(input("1. = "))

req01 = inputS1 > 0 
req02 = inputS1 < 5
req03 = inputS1 > 8
req04 = inputS1 < 11

reqAll1 = (req01 and req02 or req03 and req04)

print(f"> 0; < 5; or > 8; < 11  = {reqAll1}" )


### +++++0------5++++++8-----11+++++
inputS2 = int(input("2. = "))
arwanzxp = 10

syarat1 = inputS2 < 0 
syarat2 = inputS2 > 5
syarat3 = inputS2 < 8
syarat4 = inputS2 > 11








