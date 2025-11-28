'''Type hints untuk fungsi'''


# # default function -> studi case

# def Fungsi(num1):
#     result = num1 * 2
#     print(result)
    
# Fungsi(2)
# Fungsi("Arwanzxp") # ArwanzxpArwanzxp 

# format 
# def name_function(argument:datatype)
def Func_With_Hints(param:int): # parameter (argument) harus integer
    modulus_2 = param % 2
    return modulus_2


SisaBagi = Func_With_Hints(10) # ganti string 10, error 
print(SisaBagi)

# SisaBagi += 100
# print(SisaBagi)


