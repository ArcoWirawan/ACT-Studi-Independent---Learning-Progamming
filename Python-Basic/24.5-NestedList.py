## NESTED LIST


data_0 = [10, 20]
data_1 = [30, 40]


print(f"list = {data_0} and {data_1}")

list_on_list = [data_1,data_0,8,9]
print(f"List dalam list = {list_on_list}")



peserta_1 = ["Arwanzxp",20,"L"]
peserta_2 = ["Dazz", 19,"L"]
peserta_3 = ["Vanz",21,"L"]

all_peserta = [peserta_1, peserta_2, peserta_3]
print(f"Peserta CTF : {all_peserta}") ## Print list masih menyatu



for ctf_player in all_peserta:
    print(f"nama ={ctf_player[0]}")
    print(f"Umur ={ctf_player[1]}")
    print(f"Jenis Kelamin [L/P] = {ctf_player[2]}\n")

print('\n\n')


# with reference
list_player = all_peserta.copy()

peserta_1[0] = "aarwannzxp"
print(list_player)
print(all_peserta)
