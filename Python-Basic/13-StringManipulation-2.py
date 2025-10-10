##
"""
Kumpulan fungsi!!
1. isalpha = check all alfabet
2. isalnum = alfabet and number
3. isdecimal() = always check number
4. isspace() = check space, tab, newline (ex : \n, \t dst)
5. istitle() =  check all alphabet start from upper case
6. lower() = lower case alfabhet (abcd...)
7. upper() = upper case alfabhet(ABCD...)
8. join() -> "separator".join(namevar)
9. split("separator" "max split")
"""

# A. Operator dalam bentuk method

## merubah case dari string

# 1. merubah semua ke upper case
sapa_satpam = "permisi pak!"
print(f"penulisan asli = {sapa_satpam}")
all_huruf_kapital =  sapa_satpam.upper()
print(all_huruf_kapital + "\n")


# 2. convert all to lower case
sheHasBadmood = "KELUAR KAGA LU!!"
print(sheHasBadmood.lower() + "\n") # lower function that convert text lower alfabet


# 3. lower case alfabet check
inputText = str(input("Input kata bebas = ")) 
checkLower = inputText.islower() # does this paragraph use lower case?
print(f"Status huruf = {checkLower}") 

# 4. upper case alfabet check function
Paragraph = "HAII!!"
checkUpper = Paragraph.isupper()
print(f"Apakah bpk/ibu menggunakan huruf besar {checkUpper}")


## B. isXXX method all
"""
1. isalpha = check all alfabet
2. isalnum = alfabet and number
3. isdecimal() = always check number
4. isspace() = check space, tab, newline (ex : \n, \t dst)
5. istitle() =  check all alphabet start from upper case
"""

# 5.1  used isalpha() function
input2 = input("Cek apakah alfabet semua = ")

if input2.isalpha():
    print("!!! Ya, semua input huruf alfabet !!!")
else:
    print("WARNING !!! Ada karakter/angka masuk kesini!")

# 5.5 used istitle() function
input3 = input("Pengecekan Tata Cara Penulisan Judul = ")

if input3.istitle():
    print("Oke, judul skripsi berhasil")
else:
    print("Ulang lagi untuk judul !!!!")

# 5.2 used isalnum
input4 = input("Karakter harus huruf dan angka = ")
if input4.isalnum():
    print("Oke Nickname benar")
else:
    print("Nikname tidak boleh mengandung spasi dan karakter")

# 5. used isdecimal

input5 = input("Angka = ")
if input5.isdecimal():
    print(f"Ya, angka desimal!! Angka = {input5} ")
else:
    print("Selain angka decimal dilarang!!")

#### C. startswith() and endswith ####
# for check the start and end from qoute

checkJudulSkripsi = str(input("Judul Skripsimu = "))

if checkJudulSkripsi.istitle and (checkJudulSkripsi.startswith("Penelitian") or checkJudulSkripsi.startswith("Perancangan")):
    print("Judul di Accept, lanjut buat Bab 1")
else:
    print("Judul tidak sesuai syarat, baca ulang!!")



### combine several words (menggabungkan beberapa kata) ###
"""
1. join() = menggabungkan kata
2. split() = memisahkan kata
"""

theWords = ["Aku", "Anak", "Unpam"]

# format for join() function #
theQoutedJoin = " ".join(theWords) 
print(theQoutedJoin)

theQoutedSplit = "Kenapa#Sih#Gua#Di#Stalk#Terus#!!"

#### syntax split() ####
# 1. Used separator (pembatas untuk dijadikan spasi berdasarkan katakter)
# var.split(separator, maxsplit) 
splitQoute = theQoutedSplit.split('#') # separator #
print(splitQoute)

#  2


##### rjust, ljust, center() #####
text = "Arco Wirawan".center(10, "=")
print("'"+text+"'")


#### strip() = remove spasi yang ada pada str
text = "   ArwanzXP    "
print("Teks awal = ",text)
trimText = text.strip()
print(trimText)


## opsi strip()






